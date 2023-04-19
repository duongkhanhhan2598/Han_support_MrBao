import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import requests
import base64
import pandas as pd



def func_get_log_card_issue(req_obj):
    list_phone = req_obj.get('listPhone', [])
    current_token = req_obj.get('currentToken', '')
    if list_phone:
        try:
            list_log_data = []
            for phone in list_phone:
                # Call API Get Customer Retail
                url = 'https://apimgmt.ubank.vn/api/v1/fin/customer/retail'
                bearer_token = 'Bearer ' + current_token
                headers = {'Authorization': bearer_token}
                params = {'phoneNo': phone }
                resp_customer_retail = requests.request('GET', url, headers=headers, params=params)
                json_resp_cif_id = json.loads(resp_customer_retail.text)
                cif_id =  json_resp_cif_id.get('data', {}).get('data', {}).get('cifId', '')
                if cif_id:
                    # Query in table CardIssue
                    dynamodb = boto3.resource(
                        'dynamodb',
                        aws_access_key_id='',
                        aws_secret_access_key=''
                    )
                    table_card_issue = dynamodb.Table('CardIssue')
                    resp_query = table_card_issue.query(
                        KeyConditionExpression=Key('cifId').eq(cif_id)
                    )['Items']
                    if resp_query:
                        data_card_issue = resp_query[0]
                        log_card_issue = data_card_issue.get('log', {})
                        address = data_card_issue.get('address', '')
                        district = data_card_issue.get('district', '')
                        ward = data_card_issue.get('ward', '')
                        province = data_card_issue.get('province', '')
                    else:
                        log_card_issue = ''
                        address = ''
                        district = ''
                        ward = ''
                        province = ''
                    log_data = {
                        'phone': phone,
                        'cifId': cif_id,
                        'log': log_card_issue,
                        'address': address,
                        'district': district,
                        'ward': ward,
                        'province': province
                    }
                else:
                    log_data ={
                        'phone': phone,
                        'cifId': cif_id,
                        'message': 'Dont have record table Card Issue !'
                    }
                list_log_data.append(log_data)
            return {
                'statusCode': 200,
                'message': 'SUCCESS',
                'data': list_log_data
            }
        except (Exception, ClientError)  as e:
            print('FAIL =========>', e)
            return {
                'statusCode': 400,
                'message': 'FAIL!'
            }
    return {
        'statusCode': 400,
        'message': 'Missing Field !'
    }


# USE THIS FOR GET FILE EXCEL (NOT YET)
def lambda_handler(req_obj):
    file_excel = req_obj.get('fileExcel', '')
    if file_excel:
        file_excel_decode = base64.b64decode(file_excel)
        data_excel = pd.read_excel(file_excel_decode)
        df_excel = pd.DataFrame(data_excel)
        list_phone = df_excel['Additional Data'].tolist()
        if list_phone:
            list_message_excel = []
            for item in list_phone:
                phone = item[4:14]
                try:
                    url = 'https://apimgmt.ubank.vn/api/v1/fin/customer/retail'
                    bearer_token = 'Bearer ' + ''
                    headers = {'Authorization': bearer_token}
                    params = {'phoneNo': phone}
                    resp_customer_retail = requests.request('GET', url, headers=headers, params=params)
                    json_resp_cif_id = json.loads(resp_customer_retail.text)
                    cif_id = json_resp_cif_id.get('data', {}).get('data', {}).get('cifId', '')
                    # Query in table CardIssue
                    dynamodb = boto3.resource(
                        'dynamodb',
                        aws_access_key_id='',
                        aws_secret_access_key=''
                    )
                    table_card_issue = dynamodb.Table('customer_card')
                    resp_query = table_card_issue.query(
                        KeyConditionExpression=Key('cifId').eq(cif_id)
                    )['Items']
                    if resp_query:
                        log = resp_query[0].get('log', {})
                        log_request_issue = log.get('request_issue', [])
                        log_message = log_request_issue[0].get('message', '')
                        log_message_status = json.loads(log_message).get('statusCode', '')
                        if log_message_status == 400:
                            data_log_message = json.loads(log_message).get('data', '')
                            error_desc = json.loads(data_log_message).get('errorDetails','')[0].get('errorDesc','')
                            list_message_excel.append(error_desc)
                        elif log_message_status == 500:

                        elif log_message_status == 200:

                        else:




                    else:
                        card_issue_log = ''
                    # WRITE INTO FILE EXCEL


                except (Exception, ClientError) as e:
                    print('FAIL =========>', e)
            return {
                'statusCode': 200,
                'message': 'SUCCESS',
                'data': list_log_data
            }
        return {
            'statusCode': 400,
            'message': 'No Phone in file Excel'
        }
    return {
        'statusCode': 400,
        'message': 'Missing Field !'
    }

