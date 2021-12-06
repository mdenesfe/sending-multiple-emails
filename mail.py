import os
import smtplib
from email.message import EmailMessage

email_id = 'yourmail@gmail.com'
email_pass = 'password'

recipient_list = ['deneme@gmail.com', 'deneme2@gmail.com']

msg = EmailMessage()
msg['Subject'] = '  Sending mail multipler '
msg['From'] = email_id
msg['To'] = recipient_list
msg.set_content('Sending Mail Multipler by mdenesfe')

for each_file in os.listdir():
    if each_file == 'mail.py':
        continue
with smtplib.SMTP_SSL('smtp.gmail.com.', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)