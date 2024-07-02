import smtplib
from email.message import EmailMessage
import ssl

# Email content
mail_content = '''Hello,

In THIS mail we used Python SMTP library.
Thank You
'''

# Email addresses and password
sender_address = "anandminu15@gmail.com"
sender_pass = '********'
receiver_address = "minuanand598@gmail.com"

# Create the email message
message = EmailMessage()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
message.set_content(mail_content)

# Attachment
attach_file_name = '/content/harrypotter.txt'  # Change this to your text file
with open(attach_file_name, 'rb') as attach_file:
    message.add_attachment(attach_file.read(),
                           maintype='application',
                           subtype='octet-stream',
                           filename=attach_file_name)

# Create SMTP session and send the email
context = ssl.create_default_context()  # Create a secure SSL context
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_address, sender_pass)
    server.send_message(message)

print('Mail Sent')










