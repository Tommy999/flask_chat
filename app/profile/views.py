from . import profile
from flask import render_template, flash, redirect, request, url_for, session
from flask.ext.login import login_required

@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    name = session['auth_user']

    return render_template('profile.html', name=name)


