import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('RetailFileMetadata')
    glue = boto3.client('glue')
    print("Event recived: ")
    print(event)

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        file_type = key.split('/')[1]

    Metadata ={
        'FileName': key.split('/')[-1],
        'FileType': file_type,
        'FileArrivalTime': datetime.utcnow().isoformat(),
        'FileStatus': 'NEW',
        'SourceBucket': bucket
    }

    Metadata['Validation'] = 'Pass' if bucket == 'retail-data-poc' else 'Fail'

    table.put_item(Item=Metadata)

    # response = glue.start_job_run(JobName='retail_sales_etl')


    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Metadata Captured!!')
    }
