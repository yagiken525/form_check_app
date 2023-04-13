import boto3
import os

# S3バケット名を設定してください。

class MYAWS():
    
    S3_BUCKET_NAME = 'streamlit-formcheck-app'
   
    def __init__(self):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
        )

    def s3_fileupload(self, local_filepath, s3_filename):
        self.s3.upload_file(local_filepath, MYAWS.S3_BUCKET_NAME, s3_filename)
        return os.path.join(MYAWS.S3_BUCKET_NAME, s3_filename)

    def s3_filedownload(self, s3_filename, local_filepath):
        self.s3.download_file(MYAWS.S3_BUCKET_NAME, s3_filename, local_filepath)
    
    def s3_listobjects(self):
        return self.s3.list_objects(Bucket=MYAWS.S3_BUCKET_NAME)