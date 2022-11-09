import os
import pytest
import comp630 
import boto3
from moto import mock_s3

# test bucket specific to class and person
TEST_BUCKET = "comp630-m1-f22-jmr1178"
TEST_FILE = "jmr1178.moto"

@mock_s3
def test_upload():
    # make scope global
    global TEST_BUCKET
    global TEST_FILE
    # With the moto library imported, the boto3 s3 is fake
    conn = boto3.client("s3", region_name="us-east-1", aws_access_key_id='test', aws_secret_access_key='test', aws_session_token='test')
    # We need to create the bucket since this is all in Moto's 'virtual' AWS account
    conn.create_bucket(Bucket=TEST_BUCKET)
    with open(TEST_FILE, "rb") as f:
        object_name = os.path.basename(f.name)
        comp630.to_the_cloud(f.name, TEST_BUCKET, TEST_FILE)

    assert True
