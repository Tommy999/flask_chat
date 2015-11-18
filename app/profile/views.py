from . import profile
from flask import render_template, flash, redirect, request, url_for, session
from flask.ext.login import login_required
from ..models import *


@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    name = session['auth_user']
    workgroup_id = User.query.filter_by(username=session['auth_user']).first()
    contact_list = User.query.filter_by(workgroup_id=workgroup_id.workgroup_id).all()
    query_set = []
    [query_set.append(elem.username) for elem in contact_list]
    return render_template('profile.html', name=name, contact_list=query_set)


