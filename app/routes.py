# This will hold most of the logic for the pages in the app
import sqlite3
from app import app, db
from flask import render_template, redirect, url_for
from app.notifications import Email
from app.models import User, Reviews
from app.forms import AccountCreation, ReviewCreation, TestForm


# Root directory route. This will always be the first page to load.
@app.route('/')
def main_page():
    # Telling it what to render out. When it gets more complex, we will be passing HTML templates within these functions
    new_form = TestForm()
    return render_template('main.html', form=new_form)


@app.route('/write', methods=['GET', 'POST'])
def write_review():
    new_review = ReviewCreation()
    if new_review.validate_on_submit():
        review = Reviews(review=new_review.review.data, location=1, user='gh')
        db.session.add(review)
        db.session.commit()
        return redirect('/')
    return render_template('writereview.html', form=new_review)


@app.route('/reviews')
def reviews():
    # Fairly sure we don't need to do this in SQLAlchemy since we can interact with the DB entries as objects
    connection = sqlite3.connect("app/able.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM reviews WHERE LOCATION='id'")
    ans = crsr.fetchall()
    for i in ans:
        print(i)
    return render_template('reviews.html')

  
@app.route('/navigation')
def navigation():
    return render_template('navigation.html')


# Account creation page route
@app.route('/register', methods=['GET', 'POST'])
def registration():
    account_creation = AccountCreation()
    if account_creation.validate_on_submit():
        user = User(username=account_creation.username.data, email=account_creation.email.data)
        user.set_password(account_creation.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('/'))
    return render_template('account-creation.html', form=account_creation)

# This is not how we should be doing this and needs to be reworked to fit in the Flask conventions
# This route points to a button which will send an email.
@app.route('/send_email_button', methods=['GET', 'POST'])
def sending_emails():
    send = Email()
    send.send_email()
    return render_template('main.html')


# Same as the send_email_button, this needs to be reworked
@app.route('/see_editor_picks', methods=['GET', 'POST'])
def retrieve_editor_picks():
    return render_template('editor-picks.html')


# I'm not sure where this is implemented? In the side naa
@app.route('/return_to_main', methods=['GET', 'POST'])
def return_to_main_menu():
    return render_template('main.html')


# Can't really explain what this does technically, but it works ¯\_(ツ)_/¯
# I just now this makes it able to run
if __name__ == '__main__':
    app.run()
