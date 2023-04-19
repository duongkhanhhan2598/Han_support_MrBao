import json
import requests

index_name = ''
doc_id = ''
url = 'HELLO URL' + '/' + index_name + '/_doc/' + doc_id
body = {
    "contractNumber": ,
    "accountNumber": ,
    "typeContract": ,
    "resultInqContract": ,
    "status": ,
    "repaymentDate": ,
    "dueDate": ,
    "minDue": ,
    "balance": ,
    "tranAmount": ,
    "resultDebit": ,
    "finTranId": ,
    "popTranId": ,
    "errorCode": ,

}
payload = json.dumps(body)
print('PAYLOAD ====>', payload)
response = requests.request('PUT', url, data=payload)