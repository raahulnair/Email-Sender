import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



senderemail = 'your_email@gmail.com'
sender_password = 'your_password'
recipient_email = 'recipient_email@example.com'
subject = 'Automated Email'
message_text = 'Hello, this is an automated email.'


def send_email():
    msg = MIMEMultipart()
    msg['From'] = senderemail
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message_text, 'plain'))


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(senderemail, sender_password)


        server.sendmail(senderemail, recipient_email, msg.as_string())
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {str(e)}')


scheduled_time = '15:30'

while True:
    current_time = time.strftime('%H:%M')
    if current_time == scheduled_time:
        send_email()
        break
    else:
        time.sleep(60)  
