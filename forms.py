from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField, BooleanField, SelectField, RadioField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired(), Length(min=5)])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember = BooleanField('Remember me', default=False)


class AllgemeinForm(Form):
    Alter = SelectField('Alter', choices=[('0-30', '0-30'), ('31-45', '31-45'), ('46+', '46+')])
    Geschlecht = RadioField('Geschlecht', choices=[('m', 'Maennlich'), ('f', 'Weiblich')])
    Bildung = SelectField('Bildung', choices=[('Kein Abschluss', 'Kein Abschluss'), ('Hauptschule', 'Hauptschule'), ('Realschule', 'Realschule'), ('Fach-Hochschulreife', 'Fach-Hochschulreife'), ('Allgemeine Hochschulreife', 'Allgemeine Hochschulreife'), ('Bachelor', 'Bachelor'), ('Master', 'Master')])
