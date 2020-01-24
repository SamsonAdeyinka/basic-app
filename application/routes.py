from flask import render_template
from application import app, db
from application.models import Names
from application.forms import SelectName

@app.route('/')
def index():
    form = SelectName()

    if from.is_submitted():
        name = Names.query.all()

    return render_template('index.html', name=name, form=form)


