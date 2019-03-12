import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
	MY_ADDRESS = "gardener.bonn@gmail.com"
	# set up the SMTP server
	s = smtplib.SMTP(host='imap.gmail.com', port=587)
	s.starttls()
	s.login(MY_ADDRESS, "roboGardener")

	# create a message
	msg = MIMEMultipart()

	# add in the actual person name to the message template
	message = "test Message"

	# Prints out the message body for our sake
	print(message)

	# setup the parameters of the message
	msg['From']=MY_ADDRESS
	msg['To']="emilb540@gmail.com"
	msg['Subject']="This is TEST"
	
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
	
	# send the message via the server set up earlier.
	s.send_message(msg)
	del msg

	# Terminate the SMTP session and close the connection
	s.quit()

if __name__ == '__main__':
    main()