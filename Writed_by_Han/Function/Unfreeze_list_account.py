import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import requests
import botocore.exceptions
import uuid
from Writed_by_Han.HELPER.static_setting import init_finacle_header


def unfreeze_list_account_from_excel(req_obj, globals_variable):
    list_account_number = req_obj.get('accountNumber', [])
    if len(list_account_number):
        try:
            list_fail_unfreeze = []
            for account_number in list_account_number:
                if account_number:
                    url = globals_variable['bb_settings_url'] + '/FIP/V1.0/banks/{}/loans/{}/AcctUnFreezeAdd'.format(globals_variable['bb_settings_BANKID'], account_number)
                    headers = init_finacle_header(globals_variable)
                    resp = requests.request('POST', url, data=json.dumps({}), headers=headers)
                    print('resp.text', resp.text)
                    if resp.status_code != 200:
                        data = json.loads(resp.text)
                        print('ERROR------>', data)
                        list_fail_unfreeze.append(account_number)
            if len(list_fail_unfreeze):
                return {
                    'statusCode': 200,
                    'body': json.dumps({
                        'status': False,
                        'errcode': 'ER01',
                        'message': 'Some accounts Unfreeze FAIL!',
                        'listFailUnfreeze': list_fail_unfreeze
                    })
                }
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'status': True,
                    'errcode': 'ER01',
                    'message': 'All unfreeze SUCCESS!'
                })
            }
        except Exception as e:
            print('ERROR UNFREEZE LIST ACCT-------->', e)
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'status': False,
                    'message': 'Internal server error'
                })
            }