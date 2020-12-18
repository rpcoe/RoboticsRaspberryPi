# maybe send log file email? idk


# import smtplib
# from email import encoders
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart

# def sendMessage(content):
#     server = smtplib.SMTP('smtp.gmail.com', 25)

#     server.ehlo()

#     with open('password.txt', 'r') as f:
#         password = f.read()

#     server.login('emailgriffinnow@gmail.com', password)

#     msg = MIMEMultipart()
#     msg['From'] = 'Griffin'
#     msg['To'] = 'emailgriffinnow@gmail.com'
#     msg['subject'] = 'A test'

#     msg.attach(MIMEText(content), 'plain')

#     text = msg.as_string()
#     server.sendmail('emailgriffinnow@gmail.com', 'emailgriffinnow@gmail.com', text)