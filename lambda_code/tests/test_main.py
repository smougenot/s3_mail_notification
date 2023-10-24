import logging

from src.config import Config
from src.main import S3EventToMailProcessor

logger = logging.getLogger(__name__)


def test_missing_event(mocked_s3client, mock_ses_client):
  logger.info('test_missing_event')
  assert S3EventToMailProcessor(event={}, config=Config())() is True


def test_one_record(mocked_s3client_with_object, mock_ses_client, bucket_name, object_key):
  logger.info('test_one_record')
  event = {
    'Records': [
      {
        's3': {
          'bucket': {
            'name': bucket_name
          },
          'object': {
            'key': object_key
          }
        }
      }
    ]
  }

  assert S3EventToMailProcessor(event=event, config=Config())() is True
