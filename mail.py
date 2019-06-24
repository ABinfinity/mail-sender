import smtplib, ssl
import getpass

port = 465
#sender_email = input("enter gmail id:--> ")
#password = getpass.getpass("Type password and press enter:-->")
receiver_email = input("enter receiver email:-->")
message = input("enter message:-->")

#create ssl connection
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
	server.login("testnath064@gmail.com", "7357$Nath")
	server.sendmail(sender_email, receiver_email, message)
