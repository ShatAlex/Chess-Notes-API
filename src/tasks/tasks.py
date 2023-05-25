import smtplib
from email.message import EmailMessage

from celery import Celery

from config import SMTP_HOST, SMTP_PORT, SMTP_PASSWORD, SMTP_USER

celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_template(username: str):
    email = EmailMessage()
    email['Subject'] = 'Еженедельный отчет от ChessNotes'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, мы составили ваш еженедельный отчет по сыгранным партиям. '
        f'Продолжайте и дальше показывать высокие результаты, так держать! 😊</h1>',
        subtype='html'
    )
    return email


@celery.task
def send_email_weekly_report(username: str):
    email = get_email_template(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
