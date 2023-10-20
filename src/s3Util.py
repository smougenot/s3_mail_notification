import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class S3Util:

  def __init__(self):
    self.client = boto3.client("s3")

  def get_object_content(self, bucket_name, object_key, encoding='utf-8'):
    logger.info(f"Getting object content {bucket_name} {object_key}")
    s3_object = self.get_object(bucket_name, object_key)
    logger.debug(f"Getting object content {bucket_name} {object_key} = {s3_object}")
    if s3_object and "Body" in s3_object:
      return s3_object["Body"].read().decode(encoding)

  def get_object(self, bucket_name, object_key):
    logger.info(f"Getting object {bucket_name} {object_key}")
    try:
      return self.client.get_object(Bucket=bucket_name, Key=object_key)
    except ClientError as ex:
      if ex.response['Error']['Code'] == 'NoSuchKey':
        logger.error(f'Not found bucket:{bucket_name}, key:{object_key}, error:{ex}')
      else:
        raise
    return None
