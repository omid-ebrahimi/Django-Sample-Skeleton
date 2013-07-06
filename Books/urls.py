
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^search/$', 'BooksApp.views.bookViews.search'),

    (r'^contact/', include('BooksApp.urls.contactUrls')),
    (r'^book/', include('BooksApp.urls.bookUrls')),
    (r'^author/', include('BooksApp.urls.authorUrls')),
    (r'^publisher/', include('BooksApp.urls.publisherUrls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
