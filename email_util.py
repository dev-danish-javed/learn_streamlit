import smtplib
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils import get_logger
from concurrent.futures import ThreadPoolExecutor
log = get_logger("mail")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
USERNAME = st.secrets["SMTP_USER_NAME"]
PASSWORD = st.secrets["SMTP_APP_PASSWORD"]
executor = ThreadPoolExecutor(max_workers=4)

def send_mail(to, subject, body, html=False):
    try:
        msg = MIMEMultipart()
        msg["From"] = "Danish Javed"
        msg["To"] = to
        msg["Subject"] = subject
        if html:
            msg.attach(MIMEText(body, "html"))
        else :
            msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)
            server.sendmail(USERNAME, to, msg.as_string())
    except Exception as e:
        log.error(f"Error while sending email: {e}")
        pass

def send_mail_async(*args, **kwargs):
    executor.submit(send_mail, *args, **kwargs)

def send_welcome_mail(user_email):
    if not user_email:
        return
    elif "@" not in user_email:
        return
    try:
        with open("assets/email-template.html", "r", encoding="utf-8") as f:
            email_body = f.read()
            send_mail_async(to=user_email, subject="Welcome to Danish's Network",
                      body=email_body, html=True)
        log.info(f"Mail sent successfully to {user_email}")
    except Exception as e:
        log.error(f"Error while sending welcome mail: {e}")