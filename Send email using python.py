import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "Python email test"
body = "This is the body of the email"

#header
message = f"""From: Sender{sender}
To: Receiver{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender,receiver,message)
    print("Email has been sent")
except smtplib.SMTPServerDisconnected:
    print("Connection unexpectedly closed")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in...")
except:
    print("Unable to send email...")