import os


class Config:
  """
  sender :
    Email of the source. Can be set using environment variable EMAIL_SENDER.
    e.g. EMAIL_SENDER=test@ep.eu
  destinations :
    Emails of the destinations. Can be set using environment variable EMAIL_DESTINATIONS.
    e.g. EMAIL_DESTINATIONS=test@ep.eu,qa@ep.eu
  encoding :
    Encoding of the content from S3. Can be set using environment variable S3_CONTENT_ENCODING.
    Defaults is utf-8
    e.g. S3_CONTENT_ENCODING=utf-8
  """

  def __init__(self, sender=None, destinations=None, encoding=None):
    self.sender = sender
    self.destinations = destinations
    self.encoding = encoding
    self.ensure_defaults()

  def ensure_defaults(self):
    if self.sender is None:
      self.sender = os.environ['EMAIL_SENDER']
    if self.destinations is None:
      self.destinations = os.environ['EMAIL_DESTINATIONS']
    if not isinstance(self.destinations, list):
      self.destinations = f"{self.destinations}".split(",")
    if self.encoding is None:
      self.encoding = os.getenv('S3_CONTENT_ENCODING', 'utf-8')
    pass
