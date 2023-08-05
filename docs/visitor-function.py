import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-counter')

def lambda_handler(event, context):
    try:
        response = table.get_item(Key={
            'record-id': '0'
        })
        item = response.get('Item')
        if item is not None and 'visitor-count' in item:
            visitor_count = item['visitor-count']
        else:
            visitor_count = 0

        visitor_count += 1

        response = table.put_item(Item={
            'record-id': '0',
            'visitor-count': visitor_count
        })

        return visitor_count
    except Exception as e:
        return f"An error occurred: {str(e)}"