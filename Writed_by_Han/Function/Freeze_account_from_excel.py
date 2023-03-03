import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
# import requests
# import botocore.exceptions
import pandas as pd
from datetime import datetime
import dateutil


def lambda_handler(event, context):
    response = freeze_excel_list_account(event)
    return response

# SU DUNG CAI NAY
def invoke_freeze_excel_list_account(req_obj):
    list_casa = req_obj.get('listCasa', [])
    if len(list_casa):
        # INVOKE LAMBDA FREEZE LIST ACCOUNT
        try:
            client = boto3.client(
                'lambda',
                aws_access_key_id='',
                aws_secret_access_key=''
            )
            lambda_arn = 'arn:aws:lambda:ap-southeast-1:273658691124:function:sop-SupportFunction-gwrkNSzcOhad'
            invoke_type = 'RequestResponse'
            input_data = {
                "env_id": "uat",
                "func_name": "freeze_list_casa",
                "data": {
                    "reasonCode": "",
                    "listCasa": list_casa
                }
            }
            response = client.invoke (
                FunctionName=lambda_arn,
                InvocationType=invoke_type,
                Payload=json.dumps(input_data)
            )
            response_from_func = json.load(response['Payload'])
            print('RESPONSE FROM INVOKE LAMBDA----------->', response_from_func)
            response_status = response_from_func.get('status', '')
            if response_status == True:
                return {
                    'statusCode': 200,
                    'status': True,
                    'message': 'SUCCESS Freeze list account !',
                    'listFreeze': list_casa
                }
            else:
                return {
                    'statusCode': 400,
                    'status': False,
                    'message': 'FAIL Freeze list account !',
                    'listFreeze': list_casa
                }
        except Exception as e:
            return {
                'statusCode': 500,
                'status': False,
                'message': 'Internal server error'
            }
    return {
        'statusCode': 400,
        'status': False,
        'message': 'MISSING FIELD !'
    }









# Task: Read file Excel --> get List CASA --> Invoke lambda function A Bao to freeze list account
def freeze_excel_list_account(req_obj):
    file_name = req_obj.get('fileName', '')
    col_casa = 'Account No.\n(for existing customer)'
    if file_name:
        #Read file excel and process
        try:
            data_excel = pd.read_excel(file_name)
            df_excel = pd.DataFrame(data_excel)
            list_excel = df_excel[col_casa].tolist()
            print('LIST CASA EXCEL---------->', list_excel)
            list_casa = []
            for row in list_excel:
                temp = '000000000000' + str(row)
                list_casa.append(temp[len(str(row)):len(str(row)) + 12])
            print('LIST CASA TRANSFERED---------->', list_casa)
            if list_casa:
                # CALL API FREEZE LIST ACCOUNT
                client = boto3.client(
                    'lambda',
                    aws_access_key_id='',
                    aws_secret_access_key=''
                )
                lambda_arn = 'arn:aws:lambda:ap-southeast-1:273658691124:function:sop-SupportFunction-gwrkNSzcOhad'
                invoke_type = 'RequestResponse'
                input_data = {
                  "env_id": "uat",
                  "func_name": "freeze_list_casa",
                  "data": {
                    "reasonCode": "00006",
                    "listCasa": list_casa
                  }
                }
                response = client.invoke (
                    FunctionName = lambda_arn,
                    InvocationType = invoke_type,
                    Payload = json.dumps(input_data)
                )
                response_from_api = json.load(response['Payload'])
                print('RESPONSE FROM INVOKE LAMBDA----------->', response_from_api)
                return {
                    'status': True,
                    'message': 'SUCCESS Freeze list account !',
                    'listFreeze_receive': list_casa
                }
            return {
                'status': False,
                'message': 'List CASA is empty !'
            }
        except Exception as e:
            print('CANNOT FREEZE ACCOUNT----------->', e)
            return {
                'status': False,
                'message': 'Cannot Freeze list account'
            }
    return {
        'status': False,
        'message': 'Missing Field !'
    }