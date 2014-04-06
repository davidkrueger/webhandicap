from django.conf.urls.defaults import *


#import the login stuff
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    (r'^$', 'pollango.poll.views.handicaps'),
	(r'^add_score/$', 'pollango.poll.views.add_scores'),
	(r'^register/$', 'pollango.poll.views.test_register_user'),
	(r'^view_scores/$', 'pollango.poll.views.view_scores'),
    (r'^view_single_score/$', 'pollango.poll.views.view_single_score'),
	(r'^add_course/$', 'pollango.poll.views.add_courses'),
    (r'^edit_score/(\d*)/$', 'pollango.poll.views.edit_scores'),
    (r'^delete_score/(\d*)/$', 'pollango.poll.views.delete_score'),
    (r'^edit_course/(\d*)/$', 'pollango.poll.views.edit_course'),
    (r'^plot_handicap/$', 'pollango.poll.views.plot_handicap'),
    (r'^course_handicap/$', 'pollango.poll.views.course_handicap'),
    (r'^test_post/$', 'pollango.poll.views.test_get'),
    (r'^quotes/$', 'pollango.poll.stock_quotes.run'),
    (r'^grevocab/$', 'pollango.poll.views.show_words_for_app'),
    (r'^add_vocab_word/$', 'pollango.poll.views.add_vocab_word'),
    (r'^ajax_test/$', 'pollango.poll.views.ajax_test'),
    (r'^ajax_test_do_something/$', 'pollango.poll.views.ajax_test_do_something'),
    (r'^youtube_search', 'pollango.youtube_upload.youtube_views.search'),
    (r'^youtube', 'pollango.youtube_upload.youtube_views.show_embedded_list'),
    
    #(?P<username>[^\.^/]+)
    )
	
#use /_ah/admin to get to the admin interface