import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mail_content = '''Hello,


In THIS mail we used Python SMTP library.
Thank You
'''
# The mail addresses and password
sender_address = "manuanandam15998@gmail.com"
sender_pass = 'kjoqpfkedpxnxntg'
receiver_address = "minuanand598@gmail.com"

# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'

# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))

attach_file_name = 'smtptext.txt'  # Change this to your text file
attach_file = open(attach_file_name, 'rb')  # Open the file in bynary mode
payload = MIMEBase('application', 'octet-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)  # encode the attachment

# add payload header with text file name
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
session.starttls()  # enable security
session.login(sender_address, sender_pass)  # login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')









