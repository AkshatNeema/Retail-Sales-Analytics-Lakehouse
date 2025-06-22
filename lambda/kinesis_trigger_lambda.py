# Lambda function to process Kinesis data
def lambda_handler(event, context):
    for record in event['Records']:
        print(record['kinesis']['data'])