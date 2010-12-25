from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Entry, Feed
import datetime

def pub_dttm_desc(a, b):
    return cmp(b[0].pub_dttm, a[0].pub_dttm)

def index(request):
    feed_list = Feed.objects.all()
    entry_list = Entry.objects.select_related().filter(pub_dttm__gte=datetime.date.today()-datetime.timedelta(14)).order_by('-pub_dttm', '-id')

    # Create as dict tree 
    dict_tree = {}
    for e in entry_list:
        dict_tree.setdefault(e.pub_date(), {}).setdefault(e.feed_id, []).append(e)
    days = dict_tree.keys()
    days.sort()
    days.reverse()

    # Recreate as list tree
    recent_list = []
    for day in days:
        blog_list = [dict_tree[day][k] for k in dict_tree[day]]
        blog_list.sort(pub_dttm_desc)
        recent_list.append(blog_list)
        
    return render_to_response('planet/index.html',
            {'feed_list':feed_list, 'recent_list':recent_list})
