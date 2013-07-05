
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^search/$', 'BooksApp.views.bookViews.search'),

    (r'^contact/', include('BooksApp.urls.contactUrls')),
    (r'^contact/', include('BooksApp.urls.bookUrls')),
    (r'^contact/', include('BooksApp.urls.authorUrls')),
    (r'^contact/', include('BooksApp.urls.publisherUrls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
