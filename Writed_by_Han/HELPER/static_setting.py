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

def gen_uuid():
    return str(uuid.uuid4())

def init_finacle_header(globals_variable):
    return {
        'REQUESTUUID': gen_uuid(),
        'GLOBALUUID': gen_uuid(),
        'BUSINESSCHANNELID': globals_variable['bb_settings_BUSINESSCHANNELID'],
        'USERID': globals_variable['bb_settings_USERID'],
        'ACCESSTOKEN': globals_variable['bb_settings_access_token'],
        'x-api-key': globals_variable['bb_settings_api_key'],
        'Content-Type': 'application/json'
    }