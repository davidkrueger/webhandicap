from django.http import HttpResponse, HttpResponseRedirect
from pollango.poll import models
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from google.appengine.ext import db
import datetime
from django.contrib.auth.decorators import login_required


from google.appengine.api import users
from django.contrib.auth.forms import UserCreationForm

import wsgiref.handlers
from google.appengine.ext import webapp

import gdata.youtube
import gdata.youtube.service
import gdata.alt.appengine

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

#user authentication: https://docs.djangoproject.com/en/dev/topics/auth/default/

def upload(request):
    return
#look here: https://developers.google.com/youtube/articles/youtube_api_appengine
#and here: https://developers.google.com/youtube/1.0/developers_guide_python

def search(request):
    
    user = users.get_current_user()
    payload = dict()
    payload['user_name'] = user
    
    #youtube
    client = gdata.youtube.service.YouTubeService()
    #gdata.alt.appengine.run_on_appengine(client) #don't think I need this
    query = gdata.youtube.service.YouTubeVideoQuery()
    
    query.vq = 'beatles'
    query.orderby = 'relevance'
    query.max_results = 5
    query.start_index = 1
    #query.author = 'web2phone'
    payload['query'] = query.vq
    feed = client.YouTubeQuery(query)
    videos = []
    for v in feed.entry:
        video = {}
        video['swfurl'] = v.GetSwfUrl()
        video['title'] = v.title.text
        video['category'] = v.media.category[0]
        video['published_date'] = v.published.text.split('T')[0] + ' at ' + v.published.text.split('T')[1][:5] + ' PST'
        video['media_keywords'] = v.media.keywords
        videos.append(video)
    payload['videos'] = videos
    return render('youtube_search.html', request, payload, 'add_score')


def show_embedded_list(request):
    user = users.get_current_user()
    payload = dict()
    payload['user_name'] = user
    
    #youtube
    client = gdata.youtube.service.YouTubeService()
    gdata.alt.appengine.run_on_appengine(client)
    feed = client.GetRecentlyFeaturedVideoFeed()
    videos = []
    for v in feed.entry:
        video = {}
        video['swfurl'] = v.GetSwfUrl()
        video['message'] = v.title.text
        video['category'] = v.media.category[0]
        video['published_date'] = v.published.text.split('T')[0] + ' at ' + v.published.text.split('T')[1][:5] + ' PST'
        video['media_keywords'] = v.media.keywords
        videos.append(video)
    payload['videos'] = videos
    return render('youtube_list.html', request, payload, 'add_score')