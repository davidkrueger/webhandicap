from django.http import HttpResponse, HttpResponseRedirect
from pollango.poll import models
import bforms
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from google.appengine.ext import db
import datetime
from django.contrib.auth.decorators import login_required


from google.appengine.api import users
from django.contrib.auth.forms import UserCreationForm

def render(template, request, payload={}, active = 'home', ):
    user = users.get_current_user()
    if user:
        payload['user'] = user.nickname()
    logout_url = users.create_logout_url('/')
    payload[active] = 1
    payload['logout_url'] = logout_url
    payload['login_url'] = users.create_login_url('/')
    return render_to_response(template, payload)


  
from django.shortcuts import render_to_response


def update(request):
    return render('web.html', request)