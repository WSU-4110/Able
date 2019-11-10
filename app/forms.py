# This will hold any and all form templates
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User
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


class ReviewCreation(FlaskForm):
    review = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class TestForm(FlaskForm):
    box = StringField('Text to take from')
