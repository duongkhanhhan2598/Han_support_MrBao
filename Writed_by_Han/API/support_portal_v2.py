import json
import requests
import uuid



# UAT Environment
globals_variable = {
    'bb_settings_BUSINESSCHANNELID': 'COR',
    'bb_settings_BANKID': '01',
    'bb_settings_access_token': '',
    'bb_settings_USERID': 'FIVUSR',
    'bb_settings_url': 'https://awfcoylouaapi1.evoncloud.com/uatbkbase/finbranch-fip-ac',
    'bb_settings_api_key': 'q3t2UQRKSq6IwXAXVc2F259SUvROHeaL4BtMLo3E'
}
# TEST CUA HAN
req_obj = {
    'cifId': '555313766',
    'accountNumber': '000000002881'
}



# HELPER
def gen_uuid():
    return str(uuid.uuid4())




def get_balance(globals_variable, req_obj):
    cif_id = req_obj.get('cifId', '')

    if not cif_id:
        return{
            'statusCode': 400,
            'message': 'Missing Field !'
        }
    try:
        url = globals_variable['bb_settings_url'] + '/FIP/V1.0/banks/{}/deposits/customer/{}'.format(globals_variable['bb_settings_BANKID'], cif_id)
        headers = {
            'REQUESTUUID': gen_uuid(),
            'GLOBALUUID': gen_uuid(),
            'BUSINESSCHANNELID': globals_variable['bb_settings_BUSINESSCHANNELID'],
            'USERID': globals_variable['bb_settings_USERID'],
            'ACCESSTOKEN': globals_variable['bb_settings_access_token'],
            'x-api-key': globals_variable['bb_settings_api_key'],
            'Content-Type': 'application/json'
        }
        response = requests.request('GET', url, headers=headers)
        print('RESPONSE STATUS======>', response)
        if response.status_code != 200:
            print("ERROR STATUS =====>", response.status_code)
            print("ERROR RESPONSE =====>", response.text)
            print('ERROR CALL FIN WITH CIFID=====>', cif_id)
            return{
                'statusCode': 400,
                'message': 'Error Call FIN'
            }
        json_response = json.loads(response.text)
        print('RESPONSE DATA======>', response.text)
        if not json_response:
            print('NOT FOUND DATA OF CIFID =======>', cif_id)
            return {
                'statusCode': 400,
                'message': 'Not Found Data'
            }
        data_response = json_response.get('data', {}).get('CustAcctDtlsInqRs', {})
        if data_response:
            td_balance = 0
            interest_balance = 0
            stable_balance = 0
            total_balance = 0
            # total_balance = TotalBalance
            total_balance = data_response.get('TotalBalance', '') if data_response.get('TotalBalance', None) else data_response.get('TotalBalance ', '')
            # td_balance = TD02
            td_balance = data_response.get('TD002Balance', '') if data_response.get('TD002Balance', None) else data_response.get('TD002Balance ', '')
            acc_ll_rec = data_response.get('CustAccLLRec', [])
            if not acc_ll_rec:
                return {
                    'statusCode': 200,
                    'data': {
                        "td_balance": td_balance,
                        "interest_balance": interest_balance,
                        "stable_balance": stable_balance,
                        "total_balance": total_balance
                    }
                }
            for item in acc_ll_rec:
                scheme_code = item.get('SchmCode', '')
                if scheme_code == 'CA001':
                    # stable_balance = CA0001
                    stable_balance = item.get('Balance', '')
                elif scheme_code == 'TD001':
                    # interest_balance = TD01
                    interest_balance += item.get('Balance', '')
            return {
                'statusCode': 200,
                'data': {
                    "td_balance": td_balance,
                    "interest_balance": interest_balance,
                    "stable_balance": stable_balance,
                    "total_balance": total_balance
                }
            }
    except Exception as e:
        print('ERROR =======>', e)
        return{
            'statusCode': 500,
            'message': 'Internal Server Error'
        }


def get_term_deposit(globals_variable, req_obj):
    cif_id = req_obj.get('cifId', '')

    if not cif_id:
        return {
            'statusCode': 400,
            'message': 'Missing Field !'
        }
    try:
        url = globals_variable['bb_settings_url'] + '/fincust/V1.0/banks/{}/accounts/{}'.format(globals_variable['bb_settings_BANKID'], cif_id)
        headers = {
            'REQUESTUUID': gen_uuid(),
            'GLOBALUUID': gen_uuid(),
            'BUSINESSCHANNELID': globals_variable['bb_settings_BUSINESSCHANNELID'],
            'USERID': globals_variable['bb_settings_USERID'],
            'ACCESSTOKEN': globals_variable['bb_settings_access_token'],
            'x-api-key': globals_variable['bb_settings_api_key'],
            'Content-Type': 'application/json'
        }
        response = requests.request('GET', url, headers=headers)
        print('RESPONSE ======>', response)
        if response.status_code != 200:
            print("ERROR STATUS =====>", response.status_code)
            print("ERROR RESPONSE =====>", response.text)
            print('ERROR CALL FIN WITH CIFID=====>', cif_id)
            return {
                'statusCode': 400,
                'message': 'Error Call FIN'
            }
        json_response = json.loads(response.text)
        print('RESPONSE DATA======>', response.text)
        if not json_response:
            print('NOT FOUND DATA OF CIFID =======>', cif_id)
            return {
                'statusCode': 400,
                'message': 'Not Found Data'
            }
        data_response = json_response.get('data', {})
        error_code = data_response.get('errorCode', '')
        if error_code:
            return {
                'statusCode': 400,
                'message': 'No TD'
            }
        list_inq_result = data_response.get('TDListInquiryRs', [])
        if not list_inq_result:
            return {
                'statusCode': 400,
                'message': 'No TD'
            }
        # TD001
        list_td_001 = []
        count_td_001 = 0
        # TD002
        list_td_002 = []
        count_td_002 = 0
        for item in list_inq_result:
            scheme_code = item.get('schemeCode', '')
            if scheme_code == 'TD001':
                count_td_001 += 1
                item_td_001 = {
                    'TDNumber': item.get('TDAcctNum', ''),
                    'valueDate': item.get('accountOpenDate', ''),
                    'maturityDate': item.get('maturityDt', ''),
                    'principalAmount': item.get('InitialDepositAmount', ''),
                    'interestRate': item.get('interestRate', ''),
                    'TDTenor': item.get('depositTermDays', ''),
                    'TDInterestAmount': item.get('totIntAmt', ''),
                    'UsuperTDsAmount': item.get('Balance', '')
                }
                list_td_001.append(item_td_001)
            elif scheme_code == 'TD002':
                count_td_002 += 1
                item_td_002 = {
                    'TDNumber': item.get('TDAcctNum', ''),
                    'valueDate': item.get('accountOpenDate', ''),
                    'maturityDate': item.get('maturityDt', ''),
                    'principalAmount': item.get('InitialDepositAmount', ''),
                    'interestRate': item.get('interestRate', ''),
                    'TDTenor': item.get('depositTermMonth', ''),
                    'TDInterestAmount': item.get('totIntAmt', ''),
                    'UsuperTDsAmount': item.get('Balance', '')
                }
                list_td_002.append(item_td_002)
        return {
            'statusCode': 200,
            'data': {
                'TD001': {
                    'numberOfTD': count_td_001,
                    'listTD':  list_td_001
                },
                'TD002': {
                    'numberOfTD': count_td_002,
                    'listTD': list_td_002
                }
            }
        }

    except Exception as e:
        print('ERROR =======>', e)
        return {
            'statusCode': 500,
            'message': 'Internal Server Error'
        }


def get_transaction(globals_variable, req_obj):
    cif_id = req_obj.get('cifId', '')
    account_number = req_obj.get('accountNumber', '')

    if not cif_id or not account_number:
        return {
            'statusCode': 400,
            'message': 'Missing Field !'
        }
    try:
        url = globals_variable['bb_settings_url'] + '/fincust/V1.0/banks/{}/savings/accounts/{}/transactions'.format(globals_variable['bb_settings_BANKID'], account_number)
        headers = {
            'REQUESTUUID': gen_uuid(),
            'GLOBALUUID': gen_uuid(),
            'BUSINESSCHANNELID': globals_variable['bb_settings_BUSINESSCHANNELID'],
            'USERID': globals_variable['bb_settings_USERID'],
            'ACCESSTOKEN': globals_variable['bb_settings_access_token'],
            'x-api-key': globals_variable['bb_settings_api_key'],
            'Content-Type': 'application/json'
        }
        print('url', url)
        response = requests.request('GET', url, headers=headers)
        print('RESPONSE ======>', response)
        if response.status_code != 200:
            print("ERROR STATUS =====>", response.status_code)
            print("ERROR RESPONSE =====>", response.text)
            print('ERROR CALL FIN WITH ACCT NUMBER=====>', account_number)
            return {
                'statusCode': 400,
                'message': 'Error Call FIN'
            }
        json_response = json.loads(response.text)
        print('RESPONSE DATA======>', response.text)
        if not json_response:
            print('NOT FOUND DATA OF ACCT NUMBER =======>', account_number)
            return {
                'statusCode': 400,
                'message': 'Not Found Data'
            }
        data_response = json_response.get('data', {})
        trans_inq_rs = data_response.get('AcctTrnInqRs', {})
        list_trans_rec = trans_inq_rs.get('AcctTrnRec', [])
        if not list_trans_rec:
            return{
                'statusCode': 400,
                'message': 'No Trans Info'
            }
        list_trans = []
        for item in list_trans_rec:
            effect_date = item.get('valueDate', '')
            post_date = item.get('tranDate', '')
            ref_no = item.get('tranId', '')
            trans_flag = item.get('creditDebitFlg', '')
            trans_amount = item.get('tranAmount', '')
            trans_ccy = item.get('tranCcy', '')
            trans_type = item.get('tranType', '')
            trans_status = item.get('tranStatus', '')
            trans_particular = item.get('tranParticulars', '')
            item_trans = {
                'effectiveDate': effect_date,
                'postDate': post_date,
                'referenceNo': ref_no,
                'creditDebit': trans_flag,
                'transactionAmount': trans_amount,
                'transactionCurrency': trans_ccy,
                'transactionType': trans_type,
                'transactionStatus': trans_status,
                'description': trans_particular
            }
            list_trans.append(item_trans)
        print('LIST RETURN =======>', list_trans)
        return {
            'statusCode': 200,
            'data': {
                'listTransaction': list_trans
            }
        }

    except Exception as e:
        print('ERROR =======>', e)
        return {
            'statusCode': 500,
            'message': 'Internal Server Error'
        }


def get_card_info(globals_variable, req_obj):
    cif_id = req_obj.get('cifId', '')
    account_number = req_obj.get('accountNumber', '')

    if not account_number or not cif_id:
        return {
            'statusCode': 400,
            'message': 'Missing Field !'
        }
    try:
        url = globals_variable['bb_settings_url'] + '/FIP/V1.0/banks/{}/loans/CardDtlsInq'.format(globals_variable['bb_settings_BANKID'])
        headers = {
            'REQUESTUUID': gen_uuid(),
            'GLOBALUUID': gen_uuid(),
            'BUSINESSCHANNELID': globals_variable['bb_settings_BUSINESSCHANNELID'],
            'USERID': globals_variable['bb_settings_USERID'],
            'ACCESSTOKEN': globals_variable['bb_settings_access_token'],
            'x-api-key': globals_variable['bb_settings_api_key'],
            'Content-Type': 'application/json'
        }
        params = {'AcctNum': account_number}
        print('url', url)
        response = requests.request('GET', url, headers=headers, params=params)
        print('RESPONSE ======>', response)
        if response.status_code != 200:
            print('ERROR STATUS =====>', response.status_code)
            print('ERROR RESPONSE =====>', response.text)
            print('ERROR CALL FIN WITH ACCT NUMBER=====>', account_number)
            return {
                'statusCode': 400,
                'message': 'Error Call FIN'
            }
        json_response = json.loads(response.text)
        print('RESPONSE DATA======>', response.text)
        if not json_response:
            print('NOT FOUND DATA OF ACCT NUMBER =======>', account_number)
            return {
                'statusCode': 400,
                'message': 'Not Found Data'
            }
        data_response = json_response.get('data', {})
        if not data_response:
            print('NOT FOUND DATA OF ACCT NUMBER =======>', account_number)
            return {
                'statusCode': 400,
                'message': 'Not Found Data'
            }
        card_detail_inq = data_response.get('CardDtlsInqRs', {})
        list_card = card_detail_inq.get('CdmCardLLRec', [])
        card = list_card[0]
        card_data = {
            'cardNumber': card.get('CardNum', ''),
            'cardStatus': card.get('CardStatus', ''),
            'cardRank': card.get('CardSubtype', ''),
            'cardType': card.get('CardType', '')
        }
        return {
            'statusCode': 200,
            'data': card_data
        }
    except Exception as e:
        print('ERROR =======>', e)
        return {
            'statusCode': 500,
            'message': 'Internal Server Error'
        }




