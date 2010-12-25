from django.conf.urls.defaults import *
from django.conf import settings
from feeds import RecentFeed, AtomRecentFeed
import os
feeds = {
    'rss.xml' : RecentFeed,
    'atom.xml' : AtomRecentFeed,
}

urlpatterns = patterns('',
    (r'^$', 'planetplanet.planet.views.index'),
    (r'^(.*\.xml)$', 'django.contrib.syndication.views.feed',
            {'feed_dict': feeds}),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^css/(.*\.css)$', 'django.views.static.serve', {'document_root':os.path.join(os.getcwd(), 'static/planet/css')}),
        (r'^images/(.*)$', 'django.views.static.serve', {'document_root':os.path.join(os.getcwd(), 'static/planet/images')}),
    )
