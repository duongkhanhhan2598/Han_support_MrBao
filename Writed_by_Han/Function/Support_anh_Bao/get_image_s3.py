import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import requests
import json
from botocore.exceptions import ClientError
import botocore.exceptions
import base64
from urllib.parse import urlparse
import urllib


def lambda_handler(event, context):
    response = get_img_by_phone(event)
    return response


# Input: phone + typeImage --> Query DyanmoDB --> get URL S3 of image--> return base64 image
def get_img_by_phone(req_obj):
    phone = req_obj.get('phone', '')
    type_img = req_obj.get('typeImage', '')

    if not phone or not type_img:
        return {
            'status': False,
            'error': 'Missing Field !'
        }
    else:
        if type_img == 'selfie' or type_img == 'front-nid' or type_img == 'back-nid':
            try:
                # TABLE DYNAMO
                dynamodb = boto3.resource(
                    'dynamodb',
                    aws_access_key_id='AKIARMY6GHES7OWLVBO4',
                    aws_secret_access_key='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'
                )
                customer_image_table = dynamodb.Table('customer_img')
                # S3 ACCESS
                s3 = boto3.client(
                    's3',
                    region_name='ap-southeast-1',
                    aws_access_key_id='AKIARMY6GHES7OWLVBO4',
                    aws_secret_access_key='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'
                )
                # 1. Query DyanmoDB
                resp_img = customer_image_table.query(
                    KeyConditionExpression=Key('phone').eq(phone)
                )['Items']
                print('RESPONSE QUERY DYNAMODB ------>', resp_img)
                if resp_img:
                    list_base64_img = []
                    for row in resp_img:
                        url_img_s3 = row.get(type_img, '')
                        # path_img_s3 = S3Path(url_img_s3)
                        print('URL S3 ------>', url_img_s3)
                        o = urlparse(url_img_s3, allow_fragments=False)
                        bucket_name = o.netloc
                        img_key = o.path.lstrip('/')
                        print('URL S3 BUCKET NAME ------>', bucket_name)
                        print('URL S3 KEY ------>', img_key)
                        response_obj = s3.get_object(
                            Bucket=bucket_name,
                            Key=img_key
                        )
                        url_read = response_obj['Body'].read()
                        url_base64_encode = base64.b64encode(url_read)
                        list_base64_img.append(url_base64_encode)
                    print('LIST IMG BASE64----->', list_base64_img)
                    return {
                        'status': True,
                        'message': 'SUCCESS',
                        'typeImage': type_img,
                        'data': list_base64_img
                    }
                else:
                    return {
                        'status': True,
                        'message': 'CUSTOMER NOT EXIST IN DYNAMO',
                        'typeImage': type_img,
                        'data': []
                    }
            except (Exception, ClientError) as e:
                print('--> CANNOT QUERY IN DYNAMODB !', e)
                return {
                    'status': False,
                    'error': 'ERROR QUERY !'
                }
        else:
            return {
                'status': False,
                'error': 'Type Image does not exist !'
            }
