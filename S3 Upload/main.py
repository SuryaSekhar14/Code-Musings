import boto3
import os
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Create an S3 client
try:
    s3 = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
    )
    print("S3 client created")
except Exception as e:
    print(e)

# Upload a file to the S3 bucket
file_name = 'example.txt'
bucket_name = 'media.beesbuzz.org'
try:
    s3.upload_file(file_name, bucket_name, "test.txt")
    print("File uploaded")
except Exception as e:
    print(e)