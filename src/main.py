import logging

from src.config import Config
from src.mailUtil import MailUtil
from src.s3Util import S3Util

logger = logging.getLogger(__name__)


class S3EventToMailProcessor:

  def __init__(self, event, config: Config):
    self.config = config
    if "Records" in event:
      self.records = event["Records"]
    else:
      self.records = []
    self.s3_util = None

  def __call__(self):
    logger.info("Start processing")

    result = True
    for record in self.records:
      logger.debug(f"Processing {record}")

      if "s3" in record:
        record_s3 = record["s3"]
        if "bucket" in record_s3 and "object" in record_s3:
          if "name" in record_s3["bucket"] and "key" in record_s3["object"]:
            bucket_name = record_s3["bucket"]["name"]
            object_key = record_s3["object"]["key"]

            response = self._send_mail(bucket_name, object_key)

            if not response["ResponseMetadata"]["HTTPStatusCode"] == 200:
              logger.error(
                f"Error sending mail for s3://{bucket_name}/{object_key} to {self.config.sender} : {response}")
              result = False

    return result

  def _s3_utils(self):
    if self.s3_util is None:
      self.s3_util = S3Util()
    return self.s3_util

  def _send_mail(self, bucket_name, object_key):
    mail_util = MailUtil(sender=self.config.sender, receivers=self.config.destinations)
    # TODO manage subject
    mail_util.subject = ""
    # TODO manage body
    mail_util.body = ""
    file_content = self._s3_utils().get_object_content(
      bucket_name=bucket_name, object_key=object_key,
      encoding=self.config.encoding)
    file_name = object_key.split("/")[-1]
    mail_util.add_attachement_file(file_name=file_name, file_content=file_content)
    response = mail_util.send_mail()
    return response
