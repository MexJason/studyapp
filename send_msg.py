import email, smtplib, ssl
from providers import PROVIDERS

def send_sms(number,
             message,
             provider,
             sender_credentials,
             subject = "Sent from StudyApp",
             smtp_server = "smtp.gmail.com",
             smtp_port = 465):

    sender_email, email_password = sender_credentials
    receiver_email = f"{number}@{PROVIDERS.get(provider).get('mms')}"

    email_msg = f"Subject: {subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_msg)

def main_fun():
    number = "XXXXXXXX"
    message = "Hello World!"
    provider = "Cricket Wireless"
    sender_credentials = ("XXXXXX@XXXXX.com", "XXXXX")
    send_sms(number, message, provider, sender_credentials)



if __name__ == '__main__':
    main_fun()