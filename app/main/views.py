from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from . import main
from .forms import NameForm
from app import db
from app.models import User, Role
from flask.ext.login import login_required
from flask.ext.login import current_user

@main.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            us_role = Role.query.filter_by(name='user').first()
            user = User(username=form.name.data, role=us_role)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name']  =form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())

