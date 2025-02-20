import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config_utils import get_email_credentials


def send_email(to_email, subject, body):

#nikhilaggarwal298@gmail.com

    try:
        email_id, email_password = get_email_credentials()
    except ValueError as e:
        print(f"Error: {e}")

    msg = MIMEMultipart()
    msg["From"] = email_id
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))


    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_id, email_password)
        server.sendmail(email_id, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
send_email("ankitdungarwal92@gmail.com", "Test Subject", "This is a test email from Python.")
