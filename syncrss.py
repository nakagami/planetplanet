#!/usr/bin/env PYTHONPATH=../ python
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'

import sys, urllib2, datetime
import feedparser
from planet.models import Feed, Entry

NOW = datetime.datetime.utcnow()

if len(sys.argv) == 2:
    proxy_handlers = [urllib2.ProxyHandler({"http":"http://" + sys.argv[1]+"/"})]
else:
    proxy_handlers = None

for f in Feed.objects.all():
    # Sync RSS feed.
    if proxy_handlers:
        d = feedparser.parse(f.rss_url, handlers = proxy_handlers)
    else:
        d = feedparser.parse(f.rss_url)

    if d['feed'].get('title'):
        f.title = d.feed.title
    if d['feed'].get('link'):
        f.link = d.feed.link
    if d['feed'].get('subtitle'):
        f.subtitle = d.feed.subtitle
    if d['feed'].get('author'):
        f.author = d.feed.author
    f.save()

    # Sync feed entries.
    for e in d.entries:
        t = e.get('updated_parsed') 
        if t:
            t = datetime.datetime(*t[:7])
            if t > NOW:
                continue
        o = Entry.objects.filter(link=e.link)
        if o:
            o = o[0]                # Find a entry (probably 1 entry)
        else:
            o = Entry(feed_id=f.id) # Add new entry
            o.link = e.get('link')
        o.title = e.get('title')
        o.description = e.get('description', '')
        o.author = e.get('author', '')
        if t: 
            o.pub_dttm = t
            if f.pub_dttm_offset:
                o.pub_dttm += datetime.timedelta(0, f.pub_dttm_offset * 60)
        elif not o.pub_dttm:
            o.pub_dttm = NOW
        o.save()
