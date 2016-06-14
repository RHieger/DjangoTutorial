# Import url from Django.

from django.conf.urls import url

# Import views.

from . import views

# Create urlpattern for index page.

# Create a namespace for the polls app views:

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # the 'name' value as called by the {% url %} template tag
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
