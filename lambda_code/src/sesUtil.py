from email.mime.multipart import MIMEMultipart

import boto3


class SesUtil:

  def __init__(self):
    self.client = boto3.client("ses")

  def send_mail(self, source, destinations, msg: MIMEMultipart):
    """
    Sends Email
    :param source:
    :param destinations:
    :type msg: MIMEMultipart
    """
    response = self.client.send_raw_email(
      Source=source,
      Destinations=destinations,
      RawMessage={"Data": msg.as_string()}
    )
    return response
