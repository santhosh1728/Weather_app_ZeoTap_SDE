# email_alerts.py

import smtplib
from email.mime.text import MIMEText

def send_email_alert(city, condition, temp):
    msg = MIMEText(f"Alert for {city}: {condition} with temperature {temp:.2f}°C")
    msg['Subject'] = f"Weather Alert for {city}"
    msg['From'] = "neha7work@gmail.com"  # Replace with your email address
    msg['To'] = "nehasaniya465@gmail.com"  # Replace with recipient's email address

    # Replace with your SMTP server details
    smtp_server = 'smtp.your-email-provider.com'
    smtp_port = 587
    smtp_user = 'neha7work@gamil.com'
    smtp_password = 'neha0724@@'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")
