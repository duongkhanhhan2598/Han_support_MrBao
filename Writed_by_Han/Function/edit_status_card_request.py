import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError



def edit_status_card_request(req_obj):
    cif_id = req_obj.get('cifId', '')
    result = req_obj.get('result', '')

    if not cif_id or not result:
        return {
            'statusCode': 400,
            'message': 'Missing Field !'
        }
    try:
        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id='',
            aws_secret_access_key=''
        )
        table_card_request = dynamodb.Table('CardRequest')
        resp_query = table_card_request.query(
            KeyConditionExpression=Key('cifId').eq(cif_id)
        )['Items']
        if resp_query:
            status_card_request = resp_query[0].get('status', '')
            print('CURRENT STATUS ===========>', status_card_request)
            if result.lower() == 'approved':
                status_card_request = 'success'
            elif result.lower() == 'endcall':
                status_card_request = 'receive'
            response_update = table_card_request.update_item(
                Key={
                    'cifId': cif_id
                },
                UpdateExpression="set #ts1 = :val1",
                ExpressionAttributeNames={
                    '#ts1': 'status'
                },
                ExpressionAttributeValues={
                    ':val1': status_card_request
                }
            )
            print('RESPONSE UPDATE========> ', response_update)
            return {
                'statusCode': 200,
                'message': 'SUCCESS !',
                'statusUpdated': status_card_request
            }

        return {
            'statusCode': 400,
            'message': 'CIFID NOT EXIST !'
        }
    except (Exception, ClientError) as e:
        print('ERROR =========>', e)
        return {
            'statusCode': 400,
            'message': 'FAIL !'
        }


