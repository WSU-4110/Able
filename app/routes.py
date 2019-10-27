# This will hold most of the logic for the pages in the app
from app import app, db
from flask import render_template, redirect, url_for
from app.models import User
from app.forms import AccountCreation

# Root directory route. This will always be the first page to load.
@app.route('/')
def main_page():
    # Telling it what to render out. When it gets more complex, we will be passing HTML templates within these functions
    return render_template('main.html')


# Account creation page route
@app.route('/register', methods=['GET', 'POST'])
def registration():
    account_creation = AccountCreation()
    if account_creation.validate_on_submit():
        user = User(username=account_creation.username.data, email=account_creation.email.data)
        user.set_password(account_creation.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('account-creation.html', form=account_creation)


# Can't really explain what this does technically, but it works ¯\_(ツ)_/¯
# I just now this makes it able to run
if __name__ == '__main__':
    app.run()
