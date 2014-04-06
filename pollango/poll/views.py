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

def login_required(fn):
    #checks to see if the user is logged in, if not, redirect to login
    def _dec(view_func):
        def _checklogin(request, *args, **kwargs):
            user = users.get_current_user()
            if user:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(users.create_login_url('/'))
        _checklogin.__doc__ = view_func.__doc__
        _checklogin.__dict__ = view_func.__dict__
        return _checklogin
    return _dec(fn)


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
    

    
    
def handicaps(request):
    return render('base_handicap.html', request)

def calculate_differential(score):
    return (score.gross_score - score.rating)*113/score.slope

@login_required
def add_scores(request):
    user = users.get_current_user()
    if request.method == 'POST':
        form = bforms.addScoreForm(request.POST)
        payload = dict()
        #return render('add_score.html', request, payload, 'add_score')
        if form.is_valid():
            score = form.save(commit=False)
            score.user = user
            score.slope = score.course.slope
            score.rating = score.course.rating
            score.par = score.course.par
            score.handicap_diff = calculate_differential(score)
            score.save()
            return HttpResponseRedirect('/view_scores/')
    else:
        payload = dict()
        payload['user_name'] = user
        form = bforms.addScoreForm()
        form.number = db.IntegerProperty(default=1)
        payload['form'] = form
    return render('add_score.html', request, payload, 'add_score')

@login_required
def edit_scores(request, id):
    user = users.get_current_user()
    score = models.score.get_by_id(int(id))
    #check if correct user is editing the id
    if score.user != user:
        return HttpResponseRedirect('/view_scores/')
    if request.method == 'POST':
        form = bforms.addScoreForm(request.POST)
        if form.is_valid():
            score.course = form.cleaned_data['course']
            score.date = form.cleaned_data['date']
            score.gross_score = form.cleaned_data['gross_score']
            score.fairways_hit = form.cleaned_data['fairways_hit']
            score.greens_hit = form.cleaned_data['greens_hit']
            score.putts = form.cleaned_data['putts']
            score.user = user
            score.slope = score.course.slope
            score.rating = score.course.rating
            score.par = score.course.par
            score.handicap_diff = (score.gross_score - score.rating)*113/score.slope
            score.save()
            return HttpResponseRedirect('/view_scores/')
    else:
        form = bforms.addScoreForm(instance = score)
         
    return render('edit_score.html', request, {'form':form})

    
def calculate_handicap_from_user(user):
    #check to make sure this is the most recent 20
    scores = models.score.all().order('-date').filter('user =',user)
    scores = list(scores)
    
    for score in scores:
        score.differential = float(int(calculate_differential(score)*10))/10
    return calculate_handicap(scores)
@login_required   
def view_scores(request):
    user = users.get_current_user()
    #check to make sure this is the most recent 20
    scores = models.score.all().order('-date').filter('user =',user)
    scores = list(scores)
    
    for i, score in enumerate(scores):
        score.differential = float(int(calculate_differential(score)*10))/10
        score.num = i + 1
        
    data = calculate_handicap(scores)
    payload = dict(scores = scores, handicap = data, user = user)
    return render('view_scores.html', request, payload, 'view_scores')

#view the scorecard for a single score
def view_single_score(request):
    user = users.get_current_user()
    par = [4,4,4,4,4,4,4,5,5,3,3,4,4,3,3,5,5,3]
    yardage = [101, 102, 103, 104, 105, 106, 107, 1080, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]
    
    handicap = range(1,19)
    payload = dict(front_range = range(1,10), back_range = range(10,19), score = 1, front_par = par[:9], back_par = par[9:], front_yardage = yardage[:9], back_yardage = yardage[9:], front_handicap = handicap[:9], back_handicap = handicap[9:])
    payload['front_yardage_total'] = 2000
    payload['back_yardage_total'] = 3000
    payload['yardage_total'] = 5000
    payload['front_par_total'] = sum(payload['front_par'])
    payload['back_par_total'] = sum(payload['back_par'])
    payload['par_total'] = sum(payload['front_par']) + sum(payload['back_par'])
    payload['front_score'] = [3,4,5,6,3,4,5,6,3]
    payload['front_score_total'] = sum(payload['front_score'])
    payload['back_score'] = [3,4,5,6,3,4,5,6,5]
    payload['back_score_total'] = sum(payload['back_score'])
    payload['score_total'] = payload['back_score_total'] + payload['front_score_total']
    return render('view_single_score.html', request, payload, 'view_scores')

    

@login_required    
def add_courses(request):
    courses = models.course.all()

    if request.method == 'POST':
        form = bforms.addCourseForm(request.POST)
        if form.is_valid():
            form.hole_par_list = [1,2,3]
            course = form.save()
            return HttpResponseRedirect('/add_score/')
    else:
         form = bforms.addCourseForm()
    

    payload = dict(form=form)
    #add my course handicap
    user = users.get_current_user()
    if user:
        payload['user'] = user.nickname()
        scores = models.score.all().order('-date').filter('user =',user)[:20]
        handicap = calculate_handicap(scores)
        full_courses = []
        for course in courses: 
            temp = handicap * course.slope / 113
            #truncate
            temp = float(int(temp*10))/10
            course.my_handicap = temp
            full_courses.append(course)
        payload['courses'] = full_courses
    return render('add_course.html', request, payload, 'add_course')

@login_required    
def edit_course(request, id):
    course = models.course.get_by_id(int(id))

    if request.method == 'POST':
        form = bforms.addCourseForm(request.POST)
        if form.is_valid():
            course.name = form.clean_data['name']
            course.tees = form.clean_data['tees']
            course.yardage = form.clean_data['yardage']
            course.par = form.clean_data['par']
            course.slope = int(form.clean_data['slope'])
            course.rating = float(form.clean_data['rating'])
            course.save()
            return HttpResponseRedirect('/add_course/')
    else:
         form = bforms.addCourseForm(instance = course)
    payload = dict(form=form)
    return render('edit_course.html', request, payload, 'add_course')
    
from django import forms

@login_required
def course_handicap(request):
    user = users.get_current_user()
    courses = models.course.all()
    
    
    payload = {}
    payload['courses'] = courses
    
    if user:
        payload['index'] = calculate_handicap_from_user(user)
    form = bforms.courseHandicapForm()
    payload['form'] = form
    return render('course_handicap.html', request, payload)
    

def test_register_user(request):
    user = users.get_current_user()
    if user:
        logout_url = users.logout_url(request.uri)
        greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
                    (user.nickname(), logout_url))
        
    else:
        greeting = ("<a href=\"%s\">Sign in or register</a>." %
                        users.create_login_url("/"))
    return render('register.html', request, {'greeting': greeting, 'logout_url': logout_url})
    
def calculate_handicap(score_query):
    scores = list(score_query)
    scores.sort(key=lambda x:x.date, reverse=True)
    scores = scores[:20]
    num_scores = len(scores)
    #determine # of scores to use
    if num_scores >= 20:
        score_count = 10
    elif 16 < num_scores < 20:
        score_count = num_scores - 10
    elif 6 < num_scores < 17:
        score_count = int(num_scores / 2) - 2 + num_scores % 2
    elif num_scores < 7:
        score_count = 1
    #pick and average the handicap differentials being used
    arr = []
    
    scores.sort(key=lambda x:x.handicap_diff)
    scores = scores[:score_count]
    arr = scores[:score_count]
    # for score in scores:
        
    #this is silly, sort the list by differential, slice the top x
        # max_diff = -1000
        # max_diff_index = -1
        
        # if len(arr) < score_count:
            # arr.append(score)
        # else:
            # for i in range(len(arr)):
                # if arr[i].handicap_diff > max_diff:
                    # max_diff = arr[i].handicap_diff
                    # max_diff_index = i
            # if score.handicap_diff < max_diff:
                # arr[max_diff_index] = score
    #handle case with no scores
    if len(arr) == 0:
        return 0
    for score in arr:
        score.used_in_calculation = '*'
    #average the diffs
    total_diff = 0
    for i in range(len(arr)):
        total_diff += arr[i].handicap_diff
    avg_diff = total_diff/len(arr)
    #multiply by .96
    adj_diff = avg_diff * 0.96
    #truncate numbers after tenths digit
    adj_diff = float(int(adj_diff*10))/10
    return adj_diff
'''
def generate_nav_bar(request, active):
    user = users.get_current_user()
    
     <!-- put class="selected" in the li tag for the selected page - to highlight which page you're on -->
          <li class="selected"><a href="/">Home</a></li>
          <li><a href="/add_score">Add a score</a></li>
          <li><a href="/register">Log-in</a></li>
          <li><a href="/view_scores">View Scores</a></li>
          <li><a href="/add_courses">Add Course</a></li>
    if user:
        '''
@login_required
def delete_score(request, id):
    user = users.get_current_user()
    score = models.score.get_by_id(int(id))
    #check if correct user is editing the id
    if score.user == user:
        score.delete()
    return HttpResponseRedirect('/view_scores/')

@login_required
def plot_handicap(request):
    user = users.get_current_user()
    #check to make sure this is the most recent 20
    scores = list(models.score.all().order('date').filter('user =',user))
    
    scores_calc_history = []
    for score in scores:
        scores_calc_history.append(score)
        score.handicap = calculate_handicap(scores_calc_history)
        #adjust for zero-indexed javascript months
        score.month = score.date.month - 1
        score.day = score.date.day
        score.year = score.date.year
    return render('plot_handicap.html', request, {'scores':scores})

def add_vocab_word(request):

    if request.method == 'POST':
        form = bforms.addVocabForm(request.POST)
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect('/add_vocab_word/')
    else:
         form = bforms.addVocabForm()
    words = list(models.vocab_word.all().order('word'))
    payload = dict(form=form)
    payload['words'] = words
    return render('add_vocab_form.html', request, payload) 
    
def show_words_for_app(request):
    words = list(models.vocab_word.all())
    payload = dict(words=words)
    return render('word_display_for_app.html', request, payload)
    
def ajax_test(request):
    return render('ajax_test.html', request)

def ajax_test_do_something(request):
    return "result from python?"