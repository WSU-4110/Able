import smtplib

gmail_user = 'able4110group@gmail.com'  # create the gmail username

gmail_password = 'able12345'  # create the gmail password

sent_from = gmail_user
to = ['able4110group@gmail.com']
subject = 'Test Email.'
body = 'This is a test email, please do not respond.'

email_text = (sent_from, ", ".join(to), subject, body)  # create a single string from the given email components

# Have a try-catch statement in case of a faliure to send the message
# try:
server = smtplib.SMTP_SSL('smtp.gmail.com') # Connect to the gmail server
server.ehlo()  # identify ourselves to smtp gmail client
server.starttls  # secure our email with tls encryption
server.ehlo()  # re-identify ourselves as an encrypted connection
# server.set_debuglevel(True)
server.login(gmail_user, gmail_password)  # Attempt gmail login
server.sendmail(sent_from, to, email_text)  # Send the message over the server
server.close()  # Shut down the server connection

print('Email sent!')  # Let the user know that their email was sent sussessfully

# except:
    # print('Something went wrong...')