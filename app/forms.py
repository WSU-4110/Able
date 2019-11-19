# This will hold any and all form templates
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User
import smtplib
from app.models import Reviews


class AccountCreation(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        else:
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

class ReviewCreation(FlaskForm):
    review = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')
