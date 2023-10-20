import logging
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.sesUtil import SesUtil

logger = logging.getLogger(__name__)


class MailUtil:

  def __init__(self, sender, receivers):
    self.receivers = receivers
    self.sender = sender
    self.subject = ""
    self.body = ""
    self.file_attachements = {}

  def add_attachement_file(self, file_name, file_content):
    self.file_attachements[file_name] = file_content

  def send_mail(self):
    logger.info(f"send_mail to {self.sender}")
    msg = MIMEMultipart()
    msg["Subject"] = self.subject
    msg["From"] = self.sender
    msg["To"] = ",".join(self.receivers)

    body_txt = MIMEText(self.body, "html")
    msg.attach(body_txt)

    logger.info('adding attachements')
    for file_name  in self.file_attachements.keys():
      logger.info(f"adding attachement {file_name}")
      file_content = self.file_attachements[file_name]
      attachment = MIMEApplication(file_content)
      attachment.add_header("Content-Disposition", "attachment", filename=file_name)
      msg.attach(attachment)

    return SesUtil().send_mail(self.sender, self.receivers, msg)
