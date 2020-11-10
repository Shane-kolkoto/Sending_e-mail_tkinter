import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Sender of e-mail
sender_email_id = 'shanemorne@gmail.com'
#Reciver of e-mail
receiver_email_id = 'shanemorne@gmail.com'
#Password
password = input("Enter your password: ")
#e-mail start
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = receiver_email_id
msg['Subject'] = subject
body = "Hi sir completed this task\n"
body = body + "How is it at home"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s =smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(sender_email_id, password)
s.sendmail(sender_email_id, receiver_email_id, text)

s.quit()
