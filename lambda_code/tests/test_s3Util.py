import logging

from src.s3Util import S3Util

logger = logging.getLogger(__name__)


def test_get_object_content_on_missing(mocked_s3client_with_bucket, bucket_name):
  tool = S3Util()
  result = tool.get_object(bucket_name, "not_present.key")
  assert result is None


def test_get_object_content(mocked_s3client_with_object, bucket_name, object_key, object_content):
  tool = S3Util()
  s3_object_content = tool.get_object_content(bucket_name, object_key)
  assert s3_object_content and s3_object_content == object_content


def test_get_object_on_missing(mocked_s3client_with_bucket, bucket_name):
  tool = S3Util()
  result = tool.get_object(bucket_name, "not_present.key")
  assert result is None


def test_get_object(mocked_s3client_with_object, bucket_name, object_key):
  tool = S3Util()
  s3_object = tool.get_object(bucket_name, object_key)
  assert s3_object and "Body" in s3_object
