from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Please input thr name of the club:')
    description =  TextAreaField('Please input the description of the club:')
    categories =  SelectField('Add categorie for the club: ', choices=[('Soccer', 'Soccer'), ('Rescue', 'Rescue'), ('Cricket', 'Cricket')])
    submit = SubmitField('Add Club')


class PrivacyForm(FlaskForm):
    id = IntegerField('Id of the club to be removed: ' )
    privacy = BooleanField('Are you keeping it private?')
    submit = SubmitField('Selected')