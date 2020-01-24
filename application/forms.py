from flask_wft import FlaskForm
from wtforms import SubmitField
from applicatiion.models import Names

class SelectName(FlaskForm):
    submit = SubmitField('Select Name')
