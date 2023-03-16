import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


def lambda_handler(req_obj):
    ward = ''
    district = ''
    province = ''
    cif_id = ''
    if ward and district and province:
        try:
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
                resp_update = table_card_issue.update_item(
                    Key={
                        'cifId': cif_id
                    },
                    UpdateExpression="set #ts1 = :val1, #ts2 = :val2, #ts3 = :val3",
                    ExpressionAttributeNames={
                        '#ts1': 'ward',
                        '#ts2': 'district',
                        '#ts3': 'province'
                    },
                    ExpressionAttributeValues={
                        ':val1': ward,
                        ':val1': district,
                        ':val1': province
                    },
                )
                print('--> UPDATE SUCCESS ========> ', resp_update)
                return {
                    'statusCode': 200,
                    'status': True,
                    'message': 'UPDATE SUCCESS!'
                }
            print('--> CUSTOMER NOT EXIST IN CARD ISSUE ========> ', resp_query)
            return {
                'statusCode': 400,
                'status': False,
                'message': 'CUSTOMER NOT EXIST!'
            }
        except (Exception, ClientError) as e:
            print('--> CANNOT QUERY IN DYNAMODB !', e)
            return {
                'statusCode': 400,
                'status': False,
                'message': 'CANNOT UPDATE CUSTOMER ADDRESS'
            }
    return {
        'statusCode': 400,
        'status': False,
        'message': 'MISSING FIELD !'
    }
