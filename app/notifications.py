import smtplib
import abc

class Invoker:
  """
  Ask the command to carry out the request.
  """

  def __init__(self):
    self._commands = []

  def store_command(self, command):
    self._commands.append(command)

  def execute_commands(self):
    for command in self._commands:
      command.execute()

class Command(metaclass=abc.ABCMeta):
  """
  Declare an interface for executing an operation.
  """

  def __init__(self, receiver):
    self._receiver = receiver

  @abc.abstractmethod
  def execute(self):
    pass

class ConcreteCommand(Command):
  """
  Define a binding between a Receiver object and an action.
  Implement Execute by invoking the corresponding operation(s) on
  Receiver.
  """

  def execute(self):
    self._receiver.action()

class Receiver:
  """
  Know how to perform the operations associated with carrying out a
  request. Any class may serve as a Receiver.
  """

  # This is the gmail username and password we will use for our tests. It is a safe account with no affiliation to anyone.
  username = 'able4110group@gmail.com'  # create the gmail username
  password = 'able12345'  # create the gmail password

  def send_email(self):
    # Have a try-catch statement in case of a faliure to send the message
    try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Establishes a connection with the gmail server
      server.login('able4110group@gmail.com', 'able12345')  # Accesses the server function to prompt login
      server.sendmail(
        'able4110group@gmail.com',
        'able4110group@gmail.com',
        "Test Message, Do Not Respond")  # Accesses the server function to send the email
      server.quit()  # Exits out of the server so there is no trailing connection
      print('Email sent!')  # Let the user know that their email was sent sussessfully

    except:
      print('Something went wrong...')

def main(self):
  receiver = Receiver()
  concrete_command = ConcreteCommand(receiver)
  invoker = Invoker()
  invoker.store_command(concrete_command)
  invoker.execute_commands()