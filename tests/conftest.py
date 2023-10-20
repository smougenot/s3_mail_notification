import logging
import os
from tempfile import NamedTemporaryFile

import boto3
import pytest
from moto import mock_s3, mock_ses

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def aws_region():
  return "eu-west-1"


@pytest.fixture(scope="module")
def mocked_config(verified_email_addresse):
  os.environ['EMAIL_SENDER'] = verified_email_addresse
  os.environ['EMAIL_DESTINATIONS'] = "testing.destinations@ep.eu"


@pytest.fixture(scope="module")
def aws_creds(mocked_config, aws_region):
  os.environ['AWS_ACCESS_KEY_ID'] = "testing"
  os.environ['AWS_SECRET_ACCESS_KEY'] = "testing"
  os.environ['AWS_SECURITY_TOKEN'] = "testing"
  os.environ["AWS_SESSION_TOKEN"] = "testing"
  os.environ["AWS_DEFAULT_REGION"] = aws_region


@pytest.fixture(scope="module")
def mocked_s3client(aws_creds, aws_region):
  with mock_s3():
    client = boto3.client('s3', region_name=aws_region)
    yield client


@pytest.fixture(scope="module")
def bucket_name():
  return "test-bucket"


@pytest.fixture(scope="module")
def mocked_s3client_with_bucket(mocked_s3client, aws_region, bucket_name):
  mocked_s3client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration={
                                  'LocationConstraint': aws_region
                                })
  yield mocked_s3client


@pytest.fixture(scope="module")
def object_key():
  return "test-prefix/test-object"


@pytest.fixture(scope="module")
def object_content():
  return "test-content"


@pytest.fixture(scope="function")
def mocked_s3client_with_object(mocked_s3client_with_bucket, bucket_name, object_key, object_content):
  with NamedTemporaryFile(delete=True, suffix=".txt") as tmp:
    with open(tmp.name, "w", encoding="UTF-8") as f:
      f.write(object_content)

    mocked_s3client_with_bucket.upload_file(tmp.name, bucket_name, object_key)


@pytest.fixture(scope="module")
def verified_email_addresse():
  return "test@ep-test.eu"


@pytest.fixture(scope="module")
def mock_ses_client(aws_creds, verified_email_addresse):
  with mock_ses():
    client = boto3.client('ses', region_name="eu-west-1")
    client.verify_email_identity(EmailAddress=verified_email_addresse)
    yield client
