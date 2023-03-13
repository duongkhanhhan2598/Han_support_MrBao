import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import requests



def lambda_handler(req_obj):
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
                    log_card_issue = resp_query.get('log', {})
                    log_data = {
                        'phone': phone,
                        'cifId': cif_id,
                        'log': log_card_issue
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

