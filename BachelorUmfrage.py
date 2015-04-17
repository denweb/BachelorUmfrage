from bottle import redirect
from flask import Flask, render_template, flash, url_for
from database import db_session
from forms import AllgemeinForm
import config
from models import User

app = Flask(__name__)
app.debug = True
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/umfrage1', methods=['GET', 'POST'])
def umfrage1():
    form = AllgemeinForm(csrf_enabled=False)
    print form.validate_on_submit()
    if form.validate_on_submit():
        print "form validitert"
        """
        newUser = User(Alter=form.Alter.data, Geschlecht = form.Geschlecht.data, Bildung = form.Bildung.data)
        if newUser:
            print "Neuer User"
            db_session.add(newUser)
            db_session.commit()
            flash('Erfolgreich!')
            return redirect(url_for('umfrage3'))
        """
    return render_template('umfrage1.jinja', form = form)

@app.route('/test')
def test():
    return render_template('test.jinja')

@app.route('/umfrage2', methods=['GET', 'POST'])
def umfrage2():
    return render_template('umfrage2.jinja')

if __name__ == '__main__':
    app.run()