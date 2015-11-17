from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, data_required

class NameForm(Form):
    name = StringField('What is your name?', validators=[data_required()])
    submit = SubmitField('Submit')