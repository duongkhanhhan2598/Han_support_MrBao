import json
import pandas as pd
import boto3
import traceback
import requests
from datetime import datetime

globals_variable = {
    'portal_url': 'https://api-dashboard.ubank.vn',
    'portal_uat_environment': 'uat'
}



def fail_and_today_trans(token, cifId, type, dt_from, dt_to):
    try:
        # DATA ANH BAO: Trans FAIL + all TODAY
        path = 'v1/dashboard/payment/get-transaction-data'
        url = '{}/{}/{}'.format(globals_variable['portal_url'], globals_variable['portal_uat_environment'], path)
        payload = {
            'limit': 10000,
            'dateFrom': dt_from,
            'dateTo': dt_to
        }
        header = {
            'Authorization': 'Bearer ' + token
        }
        if len(cifId):
            payload['cifId'] = cifId
        if len(type):
            payload['type'] = type
        resp= requests.request('POST', url, headers=header, data=json.dumps(payload))
        data = json.loads(resp.text)
        item = data.get('items', [])
        # print('resp.text', data_ab)
        if resp.status_code != 200:
            print('ERROR------>', data)
            return {
                'status': False
            }
        else:
            return {
                'status': False,
                'data': item
            }
    except Exception as e:
        print('ERROR CALL API AB ======>', e)
        return {
            'status': False
        }

def success_yesterday_trans(token, cifId, platform, dt_from, dt_to):
    try:
        path = 'v1/dashboard/payment/get-statement-data'
        url = '{}/{}/{}'.format(globals_variable['portal_url'], globals_variable['portal_uat_environment'], path)
        payload = {
            'limit': 10000,
            'dateFrom': dt_from,
            'dateTo': dt_to
        }
        header = {
            'Authorization': 'Bearer ' + token
        }
        platform_lower = [s.lower() for s in platform]
        if len(cifId):
            payload['cifId'] = cifId
        if len(platform_lower):
            payload['type'] = platform_lower
        resp = requests.request('POST', url, headers=header, data=json.dumps(payload))
        data = json.loads(resp.text)
        # print('resp.text', data_cp)
        if resp.status_code != 200:
            print('ERROR------>', data)
            return {
                'status': False
            }
        item = data.get('items', [])
        return {
            'status': True,
            'data': item
        }
    except Exception as e:
        print('ERROR CALL API CP ======>', e)
        return {
            'status': False
        }



def export_csv_all_transaction(req_obj, globals_variable):
    # PLATFORM DEFAULT
    TUTUKA = {
        'CARD01', 'CARD02',
        'CARD03', 'CARD04',
        'CARD05', 'CARD06',
        'CARD07', 'CARD08',
        'WITH01', 'WITH02',
        'WITH03'
    }
    MOBILE_APP = {
        'CARD01', 'CARD02',
        'CARD03', 'CARD04',
        'CARD05', 'CARD06',
        'CARD07', 'CARD08',
        'ETFE01', 'FT02',
        'FT03', 'PAYBILL',
        'PMTNOWFE01', 'QR02',
        'QR03', 'RECHARGE01',
        'RECHARGE02', 'PMTIZ',
        'CW01'
    }
    NAPAS = {
        'FT02', 'QR03',
        'QR04', 'TOUP03',
        'TOUP01'
    }
    INTERNAL_UBANK = {
        'FT03', 'FT05'
    }
    IZION_INSUR = {
        'RFIZ', 'PMTIZ'
    }
    PAYOO = {
        'RECHARGE01', 'RECHARGE02',
        'PAYBILL'
    }
    FEC_REPAYMENT = {
        'ETFE01', 'PMTNOWFE01',
        'DDFE02', 'DDFECARD'
    }
    SMART_PAY = {
        'QR02'
    }
    TD = {
        'SW01', 'SW02',
        'SW03', 'SW04'
    }
    VP_BANK = {
        'DEPO01', 'DEPO02',
        'DEPO04', 'AD01',
        'CW01', 'FT05'
    }


    cifId = req_obj.get('cifId', '')
    platform = req_obj.get('platform', '')
    dt_from = req_obj.get('datetimeFrom', '')
    dt_to = req_obj.get('datetimeTo', '')


    if len(dt_from) == 0 or len(dt_to) == 0:
        return {
            'statusCode': 400,
            'status': False,
            'message': 'Missing Fields!'
        }
    try:
        # GET TOKEN
        url_token = 'https://stag-apimgmt.ubank.vn/api/v1/auth/token'
        payload_token = {
            "Username": "nguyencaole",
            "Password": "Office@220699"
        }
        resp_tk = requests.request('POST', url_token, data=json.dumps(payload_token))
        data_token = json.loads(resp_tk.text)
        token = data_token.get('data', {}).get('AccessToken', '')

        all_tran = []
        today_and_fail = []
        yest_success = []
        if platform == 'Napas':
            # Anh Bao
            today_and_fail_resp = fail_and_today_trans(token, cifId, 'napas_cashin', dt_from, dt_to)
            today_and_fail = today_and_fail_resp.get('data', [])
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, NAPAS, dt_from, dt_to)
            yest_success_data = yest_success_resp.get('data', [])
            for item in yest_success_data:
                part_tran_code = item.get('USER_PART_TRAN_CODE', '')
                tran_type = item.get('PART_TRAN_TYPE', '')
                if part_tran_code not in MOBILE_APP and tran_type != 'D':
                    yest_success.append(item)

        elif platform == 'Tutuka':
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, TUTUKA, dt_from, dt_to)
            yest_success_data = yest_success_resp.get('data', [])
            for item in yest_success_data:
                part_tran_code = item.get('USER_PART_TRAN_CODE', '')
                tran_type = item.get('PART_TRAN_TYPE', '')
                if part_tran_code not in MOBILE_APP and tran_type != 'D':
                    yest_success.append(item)

        elif platform == 'MobileApp':
            # Anh Bao
            today_and_fail_resp = fail_and_today_trans(token, cifId, 'mop_transfer', dt_from, dt_to)
            today_and_fail_resp_1 = fail_and_today_trans(token, cifId, 'card_transaction', dt_from, dt_to)
            today_and_fail = today_and_fail_resp.get('data', []) + today_and_fail_resp_1.get('data', [])
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, MOBILE_APP, dt_from, dt_to)
            yest_success_data = yest_success_resp.get('data', [])
            for item in yest_success_data:
                part_tran_code = item.get('USER_PART_TRAN_CODE', '')
                tran_type = item.get('PART_TRAN_TYPE', '')
                if part_tran_code in MOBILE_APP and tran_type == 'D':
                    yest_success.append(item)

        elif platform == 'Payoo':
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, PAYOO, dt_from, dt_to)
            yest_success_data = yest_success_resp.get('data', [])
            for item in yest_success_data:
                part_tran_code = item.get('USER_PART_TRAN_CODE', '')
                tran_type = item.get('PART_TRAN_TYPE', '')
                if part_tran_code not in MOBILE_APP and tran_type != 'D':
                    yest_success.append(item)

        elif platform == 'InternalUbank':
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, INTERNAL_UBANK, dt_from, dt_to)
            yest_success_data = yest_success_resp.get('data', [])
            for item in yest_success_data:
                part_tran_code = item.get('USER_PART_TRAN_CODE', '')
                tran_type = item.get('PART_TRAN_TYPE', '')
                if part_tran_code not in MOBILE_APP and tran_type != 'D':
                    if tran_type == 'C':
                        yest_success.append(item)

        elif platform == 'Izion':
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, IZION_INSUR, dt_from, dt_to)
            yest_success_data = yest_success_resp.get('data', [])
            for item in yest_success_data:
                part_tran_code = item.get('USER_PART_TRAN_CODE', '')
                tran_type = item.get('PART_TRAN_TYPE', '')
                if part_tran_code not in MOBILE_APP and tran_type != 'D':
                    yest_success.append(item)

        elif platform == 'FEC':
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, FEC_REPAYMENT, dt_from, dt_to)
            yest_success_data = yest_success_resp.get('data', [])
            for item in yest_success_data:
                part_tran_code = item.get('USER_PART_TRAN_CODE', '')
                tran_type = item.get('PART_TRAN_TYPE', '')
                if part_tran_code not in MOBILE_APP and tran_type != 'D':
                    yest_success.append(item)

        elif platform == 'SmartPay':
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, SMART_PAY, dt_from, dt_to)
            yest_success_data = yest_success_resp.get('data', [])
            for item in yest_success_data:
                part_tran_code = item.get('USER_PART_TRAN_CODE', '')
                tran_type = item.get('PART_TRAN_TYPE', '')
                if part_tran_code not in MOBILE_APP and tran_type != 'D':
                    yest_success.append(item)

        elif platform == 'TD':
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, TD, dt_from, dt_to)
            yest_success_data = yest_success_resp.get('data', [])
            for item in yest_success_data:
                part_tran_code = item.get('USER_PART_TRAN_CODE', '')
                tran_type = item.get('PART_TRAN_TYPE', '')
                if part_tran_code not in MOBILE_APP and tran_type != 'D':
                    yest_success.append(item)

        elif platform == 'VPBank':
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, VP_BANK, dt_from, dt_to)
            yest_success_data = yest_success_resp.get('data', [])
            for item in yest_success_data:
                part_tran_code = item.get('USER_PART_TRAN_CODE', '')
                tran_type = item.get('PART_TRAN_TYPE', '')
                if part_tran_code not in MOBILE_APP and tran_type != 'D':
                    yest_success.append(item)

        elif platform == 'All':
            # Anh Bao
            today_and_fail_resp = fail_and_today_trans(token, cifId, 'mop_transfer', dt_from, dt_to)
            today_and_fail_resp_1 = fail_and_today_trans(token, cifId, 'card_transaction', dt_from, dt_to)
            today_and_fail_resp_2 = fail_and_today_trans(token, cifId, 'napas_cashin', dt_from, dt_to)
            today_and_fail = today_and_fail_resp.get('data', []) + today_and_fail_resp_1.get('data', []) + today_and_fail_resp_2.get('data', [])
            # Chi Phuong
            yest_success_resp = success_yesterday_trans(token, cifId, [], dt_from, dt_to)
            yest_success = yest_success_resp.get('data', [])
        else:
            return {
                'statusCode': 400,
                'status': False,
                'message': 'Fail Field Platform !'
            }
        # PROCESS RESPONSE DATA
        if len(today_and_fail):
            for tran in today_and_fail:
                ext_data = tran.get('extData', {})
                log_data = tran.get('logs', {})
                # LOG DATA
                list_init = []
                list_otp_gen = []
                list_otp_vf = []
                list_process = []
                list_complete = []
                if log_data:
                    resp_init = log_data.get('init', [])
                    resp_otp_gen = log_data.get('otp_gen', [])
                    resp_otp_verified = log_data.get('otp_verified', [])
                    resp_process = log_data.get('process', [])
                    resp_completed = log_data.get('completed', [])
                    if resp_init:
                        for rc in resp_init:
                            init_data = {'datetime': rc.get('datetime', '')}
                            list_init.append(init_data)
                    elif resp_otp_gen:
                        for rc in resp_otp_gen:
                            json_mess = json.loads(rc.get('message', ''))
                            otp_gen_data = {
                                'phone': json_mess.get('phone', ''),
                                'datetime': rc.get('datetime', '')
                            }
                            list_otp_gen.append(otp_gen_data)
                    elif resp_otp_verified:
                        for rc in resp_otp_verified:
                            json_mess = json.loads(rc.get('message', ''))
                            otp_verified_data = {
                                'phone': json_mess.get('otp', ''),
                                'datetime': rc.get('datetime', '')
                            }
                            list_otp_vf.append(otp_verified_data)
                    elif resp_process:
                        for rc in resp_process:
                            process_data = {'datetime': rc.get('datetime', '')}
                            list_process.append(process_data)
                    elif resp_completed:
                        for rc in resp_completed:
                            complete_data = {'datetime': rc.get('datetime', '')}
                            list_complete.append(complete_data)
                # CREDIT/DEBIT + PLATFORM
                platform_temp = ''
                credit_debit = ''
                if tran.get('source', '') == 'mop_transfer':
                    credit_debit = 'D'
                    platform_temp = 'Mobile App'
                elif tran.get('source', '') == 'card_transaction':
                    credit_debit = 'D'
                    platform_temp = 'Mobile App'
                elif tran.get('source', '') == 'napas_cashin':
                    credit_debit = 'C'
                    platform_temp = 'Napas ECOM'
                temp = {
                    'Platform': platform_temp,
                    'Fin Transaction Id': tran.get('finRefId', ''),
                    'TUTUKA Transaction Id': ext_data.get('transaction_id', ''),
                    'Fin Transaction Date': tran.get('finRefDate', ''),
                    'From Account': tran.get('fromAccount', ''),
                    'To Account': tran.get('toAccount', ''),
                    'Create At': tran.get('createdAt', ''),
                    'Amount': tran.get('amount', ''),
                    'Credit/Debit': credit_debit,
                    'Transaction Particular': tran.get('tranParticular', ''),
                    'Account Type': tran.get('accountType', ''),
                    'Partner Id': tran.get('partnerId', ''),
                    'Bank Code': tran.get('bankCode', ''),
                    'Status': tran.get('status', ''),
                    'Reason': ext_data.get('reason', ''),
                    'Transaction Type': ext_data.get('type', ''),
                    'Merchant Category Code': ext_data.get('merchant_category_code', ''),
                    'Capture Mode': ext_data.get('capture_mode', ''),
                    'Merchant': ext_data.get('merchant', ''),
                    'TUTUKA Type': ext_data.get('type', ''),
                    'Balance': ext_data.get('balance', ''),
                    'Tracking Number': ext_data.get('tracking_number', ''),
                    'Campaign': ext_data.get('campaign', ''),
                    'Terminal Id': ext_data.get('terminal_id', ''),
                    'Init data': str(list_init).replace('[', '').replace(']', '') if len(list_init) else '',
                    'OTP_Gen data': str(list_otp_gen).replace('[', '').replace(']', '') if len(list_otp_gen) else '',
                    'OTP_Verified data': str(list_otp_vf).replace('[', '').replace(']', '') if len(list_otp_vf) else '',
                    'Process data': str(list_process).replace('[', '').replace(']', '') if len(list_process) else '',
                    'Complete data': str(list_complete).replace('[', '').replace(']', '') if len(list_complete) else ''
                }
                all_tran.append(temp)
        if len(yest_success):
            for tran in yest_success:
                # TRAN DATE
                tran_date = tran.get('TRAN_DATE', '')
                if tran.get('TRAN_DATE', ''):
                    tran_date = datetime.strptime(tran.get('TRAN_DATE', ''), '%Y-%m-%dT%H:%M:%S.%fZ')
                # TRAN AMOUNT
                tran_amount = tran.get('TRAN_AMT', '')
                if tran.get('TRAN_AMT', ''):
                    if '.' in tran.get('TRAN_AMT', ''):
                        tran_amount = tran.get('TRAN_AMT', '')[:-5]
                # PLATFORM
                platform_temp = ''
                part_tran_temp = tran.get('USER_PART_TRAN_CODE', '')
                tran_type_temp = tran.get('PART_TRAN_TYPE', '')
                if tran_type_temp == 'D' and part_tran_temp in MOBILE_APP:
                    platform_temp = 'Mobile App'
                else:
                    if part_tran_temp in TUTUKA:
                        platform_temp = 'TUTUKA'
                    elif part_tran_temp in NAPAS:
                        if part_tran_temp == 'TOUP01':
                            platform_temp = 'Napas ECOM'
                        elif part_tran_temp == 'TOUP01' and tran_type_temp == 'C':
                            platform_temp = 'Napas ECOM'
                        platform_temp = 'Napas IPFT'
                    elif part_tran_temp in PAYOO:
                        platform_temp = 'Payoo'
                    elif part_tran_temp in INTERNAL_UBANK and tran_type_temp == 'C':
                        platform_temp = 'Internal UBank'
                    elif part_tran_temp in IZION_INSUR:
                        platform_temp = 'IZION Insurance'
                    elif part_tran_temp in FEC_REPAYMENT:
                        platform_temp = 'FEC Repayment'
                    elif part_tran_temp in SMART_PAY:
                        platform_temp = 'Smart Pay'
                    elif part_tran_temp in TD:
                        platform_temp = 'TD'
                    elif part_tran_temp in VP_BANK:
                        if part_tran_temp == 'FT05' and tran_type_temp == 'D':
                            platform_temp = 'VPBank T24'
                        platform_temp = 'VPBank'

                temp = {
                    'Platform': platform_temp,
                    'Fin Transaction Id': tran.get('TRAN_ID', ''),
                    'Fin Transaction Date': tran_date,
                    'From Account': tran.get('FORACID', '') if tran.get('PART_TRAN_TYPE','') == 'D' else '',
                    'To Account': tran.get('FORACID', '') if tran.get('PART_TRAN_TYPE', '') == 'C' else '',
                    'Create At': tran.get('TRAN_DATE', '')[:-4].replace('T', ' '),
                    'Credit/Debit': tran.get('PART_TRAN_TYPE', ''),
                    'Amount': tran_amount,
                    'Transaction Particular': tran.get('TRAN_PARTICULAR', ''),
                    'Transaction Type': tran.get('TRAN_TYPE', ''),
                    'Status': 'completed',
                    'Transaction Sub Type': tran.get('TRAN_SUB_TYPE', ''),
                    'User PartTran Code': tran.get('USER_PART_TRAN_CODE', ''),
                    'Cif Id': tran.get('CIF_ID', ''),
                    'Part Tran_Result Number': tran.get('PART_TRAN_SRL_NUM', ''),
                    'Transaction Remake': tran.get('TRAN_RMKS', ''),
                    'Debit': tran.get('DEBIT', ''),
                    'Ben Customer Name': tran.get('BEN_CUST_NAME', ''),
                    'Ben Bank Id': tran.get('BEN_BANK_ID', ''),
                    'Ben Bank Name': tran.get('BEN_BANK_NAME', ''),
                    'Contract Number': tran.get('CONTRACT_NUMBER', '')
                }
                all_tran.append(temp)

        # FORMAT ALL TRANS DATA
        for item in all_tran:
            if item.get('From Account', ''):
                item['From Account'] = "'" + str(item.get('From Account', ''))
            if item.get('To Account', ''):
                item['To Account'] = "'" + str(item.get('To Account', ''))
            if item.get('Amount', ''):
                item['Amount'] = "'" + str(item.get('Amount', ''))
            if item.get('Ben Bank Id', ''):
                item['Ben Bank Id'] = "'" + str(item.get('Ben Bank Id', ''))
            if item.get('Contract Number', ''):
                item['Contract Number'] = "'" + str(item.get('Contract Number', ''))
            if item.get('Partner Id', ''):
                item['Partner Id'] = "'" + str(item.get('Partner Id', ''))
            if item.get('Balance', ''):
                item['Balance'] = "'" + str(item.get('Balance', ''))

        # FILTER AGAIN
        all_tran_filter = []
        for item in all_tran:
            if platform == 'Napas':
                if 'Napas' in item.get('Platform', ''):
                    all_tran_filter.append(item)
            elif platform == 'Tutuka':
                if 'TUTUKA' in item.get('Platform', ''):
                    all_tran_filter.append(item)
            elif platform == 'MobileApp':
                if 'Mobile App' in item.get('Platform', ''):
                    all_tran_filter.append(item)
            elif platform == 'Payoo':
                if 'Payoo' in item.get('Platform', ''):
                    all_tran_filter.append(item)
            elif platform == 'InternalUbank':
                if 'Internal UBank' in item.get('Platform', ''):
                    all_tran_filter.append(item)
            elif platform == 'Izion':
                if 'IZION' in item.get('Platform', ''):
                    all_tran_filter.append(item)
            elif platform == 'FEC':
                if 'FEC' in item.get('Platform', ''):
                    all_tran_filter.append(item)
            elif platform == 'SmartPay':
                if 'Smart Pay' in item.get('Platform', ''):
                    all_tran_filter.append(item)
            elif platform == 'TD':
                if 'TD' in item.get('Platform', ''):
                    all_tran_filter.append(item)
            elif platform == 'VPBank':
                if 'VPBank' in item.get('Platform', ''):
                    all_tran_filter.append(item)
            else:
                all_tran_filter = all_tran
        # EXPORT TO CSV
        file_name = 'Transaction_{}.csv'.format(platform)
        df = pd.DataFrame(all_tran_filter)
        df.reset_index(drop=True, inplace=True)
        df.index += 1
        df.index.name = '#'
        df.to_csv(file_name, index=True, header=True, sep='\t')
        # Insert s3
        print('EXPORT SUCCESS !!!!!!!!!')
        return {
            'statusCode': 200,
            'status': True,
            'data': 'S3 URL'
        }
    except Exception as e:
        print('ERROR=========>', e)
        traceback.print_exc()
        return {
            'statusCode': 500,
            'status': False,
            'message': 'Internal Server Error!'
        }






