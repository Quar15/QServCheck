from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from flask_login import current_user
from qcheckserv.users.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    pretty_name = StringField('Pretty Name',
                              validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_pretty_name(self, pretty_name):
        user = User.query.filter_by(pretty_name=pretty_name.data).first()
        if user:
            raise ValidationError('That pretty name is taken. Please choose a different one.')


class UserEditForm(FlaskForm):
    user_id = HiddenField('Id', validators=[DataRequired()])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    pretty_name = StringField('Pretty Name',
                              validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo('password')])
    submit = SubmitField('Update')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).filter(User.id != self.user_id.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_pretty_name(self, pretty_name):
        user = User.query.filter_by(pretty_name=pretty_name.data).filter(User.id != self.user_id.data).first()
        if user:
            raise ValidationError('That pretty name is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')