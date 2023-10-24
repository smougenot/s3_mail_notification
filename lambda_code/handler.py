import logging
from logging.config import dictConfig

from src.main import S3EventToMailProcessor
from src.logging_config import LOGGING_CONFIG

logger = logging.getLogger(__name__)
dictConfig(LOGGING_CONFIG)
logger.info('start')

def lambda_handler(event, context):
  logger.info(f'processing {event}')
  result = S3EventToMailProcessor(
    event=event
  )()
  logger.info(f'done for {event}')
  return result
