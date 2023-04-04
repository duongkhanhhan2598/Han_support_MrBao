import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import requests
import botocore.exceptions
import pandas as pd

def excel_to_opensearch(file_name):
    # Read file excel and process
    try:
        data_excel = pd.read_csv(file_name)
        df_excel = pd.DataFrame(data_excel)
        doc_id = 0
        for row in df_excel.index.tolist():
            data_row = {
                'eContractDate': df_excel['EcontractedDate'].values[row],
                'openIssueDate': df_excel['OpenIssueDate'].values[row],
                'sequenceTutuka': df_excel['SequenceTutuka'].values[row],
                'cardNumber': df_excel['Card'].values[row],
                'billCode': df_excel['BillCode'].values[row],
                'trackingNumber': df_excel['TrackingNumber'].values[row],
                'additionalData': df_excel['AdditionalData'].values[row],
                'phone': df_excel['PhoneNumber'].values[row],
                'cardHolder': df_excel['CardholderName'].values[row],
                'address1': df_excel['Address1'].values[row],
                'address2': df_excel['Address2'].values[row],
                'address3': df_excel['Address3'].values[row],
                'address4': df_excel['Address4'].values[row],
                'address5': df_excel['Address5'].values[row],
                'cardType': df_excel['TypeCard'].values[row],
                'vendorDelivery': df_excel['VendorDelivery'].values[row],
                'merchantName': df_excel['MerchantName'].values[row],
                'accountNumber': df_excel['AccountNumber'].values[row],
                'qrCode': df_excel['QRCode'].values[row],
                'cardStatus': df_excel['CardStatus'].values[row],
                'embossingStatus': df_excel['EmbossingStatus'].values[row],
                'timestamp': df_excel['Time_Stamp'].values[row],
                'note': df_excel['Notes'].values[row],
                'fileName': df_excel['FileName'].values[row],
                'user': df_excel['User'].values[row],
            }
            # Insert OPENSEARCH for Each Row
            doc_id += 1
            index_name = ''
            url = 'HELLO URL' + '/' + index_name + '/_doc/' + doc_id
            payload = json.dumps(data_row)
            print('PAYLOAD ====>', payload)
            response = requests.request('PUT', url, data=payload)
            json_response = json.loads(response.text)
            error_response = json_response.get('error', '')
            # Check error
            if len(error_response):
                print('ERROR ==>', json_response)
                print('URL ==>', url)
                print(print('PAYLOAD ==>', payload))
            else:
                print('SUCCESS INSERT', payload)
        return{
            'message': 'Done'
        }
    except Exception as e:
        print('ERROR ======>', e)
        return {
            'message': 'Can do nothing !'
        }