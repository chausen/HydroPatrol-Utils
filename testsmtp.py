import smtplib

sender = '' # your email here
password = '' # your password here
receivers = [''] # list of receivers here

message = """From: From Person <email>
To: To Person <receiver>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
   smtpObj.ehlo()
   smtpObj.login(sender, password)
   smtpObj.sendmail(sender, receivers, message)
   smtpObj.close()         
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")