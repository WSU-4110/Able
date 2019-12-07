# This will hold most of the logic for the pages in the app
import sqlite3
from app import app, db
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user
from app.notifications import Email
from app.models import User, Reviews
from app.forms import AccountCreation, ReviewCreation, Login, Contact
import smtplib


# Root directory route. This will always be the first page to load.
# We add the 'index' decorator to make it an endpoint we can hit with other functions in Flask.
# Just using '/' does not work in almost all context/situations.
@app.route('/')
@app.route('/index')
def main_page():
    # Telling it what to render out. When it gets more complex, we will be passing HTML templates within these functions
    return render_template('main.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Contact()
    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return redirect(url_for('main_page'))
    elif request.method == 'GET':
        return render_template('contact.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')


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
    reviews = Reviews.query.filter_by(location=1)
    avg = 1
    for i in reviews:
        avg = avg + i.rating
    avg = avg/(reviews.count()+1)
    return render_template('reviews.html', reviews=reviews, average=avg)


@app.route('/navigation')
def navigation():
    return render_template('navigation.html', title='Able')


# Account creation page route
@app.route('/register', methods=['GET', 'POST'])
def registration():
    account_creation = AccountCreation()
    if account_creation.validate_on_submit():
        # Creating the account in the DB if all info the form is good
        user = User(username=account_creation.username.data, email=account_creation.email.data)
        user.set_password(account_creation.password.data)
        db.session.add(user)
        db.session.commit()
        # Once someone creates their account, they're automatically logged in
        # Have to query the DB to login rather than being able to use data from registration form
        user = User.query.filter_by(username=account_creation.username.data).first()
        login_user(user)
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Establishes a connection with the gmail server
            server.login('able4110group@gmail.com', 'able12345')  # Accesses the server function to prompt login
            server.sendmail(
                'able4110group@gmail.com',
                'able4110group@gmail.com',
                "Test Message, Do Not Respond")  # Accesses the server function to send the email
            server.quit()  # Exits out of the server so there is no trailing connection

        except:
            print('Something went wrong...')
        return redirect(url_for('main_page'))
    return render_template('account-creation.html', form=account_creation)


# Another page for users to login at. Will redirect to main if already logged in.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    login_form = Login()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', form=login_form)


# Route holds functionality for logging out.
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('registration'))

# This route points to a button which will send an email
@app.route('/send_email_button', methods=['GET', 'POST'])
def sending_emails():
    send = Email()
    send.send_email()
    return render_template('main.html')

@app.route('/user_profile', methods=['GET', 'POST'])
def retrieve_user_profile():
    all_reviews = Reviews.query
    return render_template('userprofile.html', reviews=all_reviews)

# Can't really explain what this does technically, but it works ¯\_(ツ)_/¯
# I just now this makes it able to run
if __name__ == '__main__':
    app.run()
