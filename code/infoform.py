from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import date, timedelta

countries = 'Austria', 'Greece', 'Italy', 'France', 'Spain', 'United_Kingdom', 'Sweden' 
default_country = [('', 'Choose Country')]
start_date = date(2021,4,16)
dates =  [(start_date+timedelta(i)).isoformat() for i in range(30)]
default_date = [('', 'Choose Date')]

class InfoForm(FlaskForm):
    country = SelectField(u'Country destination:', [DataRequired()], choices=default_country+[(country, country) for country in countries])
    date = SelectField(u'Date of vacations:', [DataRequired()], choices=default_date+[(date, date) for date in dates])
    # date = DateField('Date of vacations?', default=datetime(2021, 4, 15))
    submit = SubmitField('Submit')
