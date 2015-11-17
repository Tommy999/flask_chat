from flask import render_template, flash, redirect, request, url_for, session
from . import auth
from .forms import LoginForm, RegisterForm
from ..models import User, Role
from flask.ext.login import login_user
from flask.ext.login import logout_user, login_required
from app import db
from flask.ext.login import current_user


@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is not None and user.verify_password(login_form.password.data):

            login_user(user, login_form.remember_me.data)
            session['auth_user'] = user.username
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('login.html', login_form=login_form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('auth_user', None)
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET','POST'])
def register():
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        role_id = Role.query.filter_by(name='user').first()
        user = User(username=reg_form.username.data, password=reg_form.password.data, role_id=int(role_id.id))
        db.session.add(user)
        db.session.commit()
        flash('You cann now login')
        return redirect(url_for('auth.login'))
    return render_template('register.html', reg_form=reg_form)
