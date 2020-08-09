import os
from flask import Flask, render_template, redirect
from forms import AddForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

db = SQLAlchemy(app)

Migrate(app, db)
##########
# Model - Name of database
class Club(db.Model):
    # Table name
    __tablename__ = 'clubs'

    #columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    categories = db.Column(db.Text)
    privacy = db.relationship('Privacy', backref='clubs', uselist=False)
    def __init__ (self, name, description, categories):
        self.name = name
        self.description = description
        self.categories = categories


    def __repr__ (self):
        if self.privacy:
            return "This Club: {}, Descrition: {}, Categioried: {}, Privacy: {}.".format(self.name, self.description, self.categories, self.privacy)
        else:
            return  "This Club: {}, Described: {}, Categioried: {}.No privacy defined.".format(self.name, self.description, self.categories)
     

class Privacy(db.Model):

    __tablename__ = 'private'

    id = db.Column(db.Integer, primary_key=True)
    setting = db.Column(db.Boolean)

    club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'))

    def __init__ (self, setting, club_id):
        self.setting = setting
        self.club_id = club_id


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_club():
    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data
        description = form.description.data
        categories = form.categories.data

        new_club = Club(name, description, categories)
        db.session.add(new_club)
        db.session.commit()

        return redirect(url_for('list_form'))

    return render_template('add.html', form=form)

@app.route('/list')
def list_form():

    clubs = Club.query.all();
    return render_template('list.html', clubs=clubs)


if __name__ == '__main__':
    app.run(debug=True)