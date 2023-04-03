import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import requests

def transfer_phone_and_cifId(req_obj):
    list_phone = req_obj.get('list_PHONE', [])
    list_cif_id = req_obj.get('list_CIFID', [])
    if not list_phone and not list_cif_id:
        return {
            'message': 'MISSING FIELDS!'
        }
    try:
        url = 'https://apimgmt.ubank.vn/api/v1/fin/customer/retail'
        bearer_token = ''
        headers = {'Authorization': bearer_token}
        list_resp = []
        # proccess PHONE ----> CIFIF
        for phone in list_phone:
            params = {'phoneNo': phone}
            resp_of_phone = requests.request('GET', url, headers=headers, params=params)
            json_resp_of_phone = json.loads(resp_of_phone.text)
            data_resp_of_phone = json_resp_of_phone.get('data', {}).get('data', {})
            cif_id_resp = data_resp_of_phone.get('cifId', '')
            phone_cif_id = {
                'phone': phone,
                'cifId': cif_id_resp
            }
            list_resp.append(phone_cif_id)
        # Proccess CIFID ----> PHONE
        for cif_id in list_cif_id:
            params = {'cifId': cif_id}
            resp_of_cif_id = requests.request('GET', url, headers=headers, params=params)
            json_resp_of_cif_id = json.loads(resp_of_cif_id.text)
            data_resp_of_cif_id = json_resp_of_cif_id.get('data', {}).get('data', {})
            phone_resp = data_resp_of_cif_id.get('customerInqRs', {}).get('phoneNo', '')
            phone_cif_id = {
                'phone': phone_resp,
                'cifId': cif_id
            }
            list_resp.append(phone_cif_id)
        return {
            'message': 'SUCCESS!',
            'data': list_resp
        }
    except Exception as e:
        print('ERROR TRANSFER PHONE AND CIFIF===========>', e)
        return {
            'message': 'FAIL CALL API!'
        }