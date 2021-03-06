from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Length, Regexp, EqualTo
from ..models import *


class LoginForm(Form):

    workgroup = StringField('Workgroupname')
    username = StringField('Username')
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me loged in')
    submit = SubmitField('Log in')


class RegisterForm(Form):

    workgroup = StringField('Workgroup', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Workgroupnames must have only letters, numbers, dots or underscores')])
    username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('User name is already in use')

    def validate_workgroup(self, field):
        if Worgroup.query.filter_by(workgroup_name=field.data).first() is None:
            raise ValidationError('Workgorup does not exist')


class CreateWorkgroup(Form):

    workgroup = StringField('Workgroup', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Workgroupnames must have only letters, numbers, dots or underscores')])
    submit = SubmitField('Create')
    def validate_workgroup(self, field):
        if Worgroup.query.filter_by(workgroup_name=field.data).first():
            raise ValidationError('Workgorupname already in use')