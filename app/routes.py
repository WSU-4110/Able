# This will hold most of the logic for the pages in the app
from app import app
from flask import render_template
from app.forms import AccountCreation

# Root directory route. This will always be the first page to load.
@app.route('/')
def main_page():
    # Telling it what to render out. When it gets more complex, we will be passing HTML templates within these functions
    account_creation = AccountCreation()
    return render_template('account-creation.html', form=account_creation)


# Can't really explain what this does technically, but it works ¯\_(ツ)_/¯
# I just now this makes it able to run
if __name__ == '__main__':
    app.run()
