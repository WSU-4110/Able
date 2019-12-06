# This will hold any and all form templates
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User
from app.models import Reviews


class Contact(FlaskForm):
    name = StringField('Name', validators=[DataRequired("Please enter your name.")])
    email = StringField('Email', validators=[DataRequired("Please enter your email address.")])
    subject = StringField('Subject', validators=[DataRequired("Please enter a subject.")])
    message = StringField('Message', validators=[DataRequired("Please enter a message.")])
    submit = SubmitField("Send")


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

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class ReviewCreation(FlaskForm):
    review = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')