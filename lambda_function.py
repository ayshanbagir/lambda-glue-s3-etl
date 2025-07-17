import boto3
import csv
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    glue = boto3.client('glue')
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    lines = response['Body'].read().decode('utf-8').splitlines()
    reader = csv.DictReader(lines)
    
    print("Processing file:", key)
    for row in reader:
        print(f"User ID: {row['id']}, Name: {row['name']}, Email: {row['email']}")
    
    glue_job_name = "csv-etl-job"
    response = glue.start_job_run(
        JobName=glue_job_name,
        Arguments={
            '--SOURCE_PATH': f's3://{bucket}/{key}',
            '--DEST_PATH': f's3://{bucket}/processed/sample/'
        }
    )

    print(f"Started Glue job: {glue_job_name} | Run ID: {response['JobRunId']}")

    return {
        'statusCode': 200,
        'body': f'Successfully processed {key} file and triggered Glue job: {glue_job_name}'
    }
