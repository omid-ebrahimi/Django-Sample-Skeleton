__author__ = 'OMID EBRAHIMI'

from django.conf.urls import url, patterns
from BooksApp.views.contactViews import contact
from BooksApp.views.contactViews import registerThanks

urlpatterns = patterns('BooksApp.views.contactViews',
    url(r"^$", contact),
    url(r"^thanks/$", registerThanks),
)