import uuid
import hashlib
import hmac
from datetime import datetime
import requests
import json

def encrypt_SHA1():
    private_key = '71F291D90E'
    now = datetime.now()
    terminal_id = '0081508954'
    device_id = str(uuid.uuid4())
    trans_id = str(uuid.uuid4())
    trans_date = now.strftime("%Y%m%dT%H:%M:%S")
    method = 'Authenticate'
    # Plus values of sorted alphabetically all keys
    content = device_id + method + terminal_id + trans_date + trans_id
    # ENCODE SHA1
    raw = content.encode("utf-8")
    key = private_key.encode("utf-8")
    hashed = hmac.new(key, raw, hashlib.sha1)
    check_sum = hashed.hexdigest()
    print("device_id ====", device_id)
    print("trans_id ====", trans_id)
    print('trans_date====', trans_date)
    print('content', content)
    print('check sum ======>',check_sum)
    # CALL API for checking
    url = 'https://stream.uat.tutuka.cloud/json'
    params = {
        'checksum': check_sum,
        'deviceID': device_id,
        'method': method,
        'terminalID': terminal_id,
        'transactionDate': trans_date,
        'transactionID': trans_id
    }
    response = requests.request('GET', url, params=params)
    print('RESPONSE =========>', json.loads(response.text))
    return response