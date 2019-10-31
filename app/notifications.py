import smtplib

class Email():

  # This is the gmail username and password we will use for our tests. It is a safe account with no affiliation to anyone.
  gmail_user = 'able4110group@gmail.com'  # create the gmail username
  gmail_password = 'able12345'  # create the gmail password
  def send_email(gmail_user, gmail_password):
    # Have a try-catch statement in case of a faliure to send the message
    try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # Establishes a connection with the gmail server
      server.login(gmail_user, gmail_password) # Accesses the server function to prompt login
      server.sendmail(
        gmail_user,
        gmail_user,
        "Test Message, Do Not Respond") # Accesses the server function to send the email
      server.quit() # Exits out of the server so there is no trailing connection
      print('Email sent!')  # Let the user know that their email was sent sussessfully

    except:
        print('Something went wrong...')

