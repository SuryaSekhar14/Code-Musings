import boto3
import os

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
)

# Upload a file to the S3 bucket
file_name = 'example.txt'
bucket_name = 'bees-app-media-storage'
s3.upload_file(file_name, bucket_name, "test.txt")