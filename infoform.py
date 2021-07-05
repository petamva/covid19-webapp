from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import date, timedelta

countries = ['Austria',
            # 'Belgium',
            # 'Bulgaria',
            'Croatia',
            'Cyprus',
            'Czechia',
            # 'Denmark',
            'Estonia',
            # 'Finland',
            'France',
            # 'Germany',
            'Greece',
            'Hungary',
            'Iceland',
            'Ireland',
            'Italy',
            # 'Latvia',
            'Lithuania',
            'Luxembourg',
            'Malta',
            'Netherlands',
            'Norway',
            # 'Poland',
            # 'Portugal',
            'Romania',
            'Slovakia',
            # 'Slovenia',
            'Spain',
            'Sweden',
            'Switzerland',
            'United Kingdom']

default_country = [('', 'Choose Country')]
start_date = date(2021,6,17)
dates =  [(start_date+timedelta(i)).isoformat() for i in range(75)]
default_date = [('', 'Choose Date')]

class InfoForm(FlaskForm):
    country = SelectField(u'Country destination:', [DataRequired()], choices=default_country+[(country, country) for country in countries])
    date = SelectField(u'Date of vacations:', [DataRequired()], choices=default_date+[(date, date) for date in dates])
    # date = DateField('Date of vacations?', default=datetime(2021, 4, 15))
    submit = SubmitField('Submit')
