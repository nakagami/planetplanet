from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from models import Entry
import datetime

class RecentFeed(Feed):
    title = "Planet Python Japan"
    link = "/planet/"
    description = "Planet Python Japan  RSS feeds."
    def items(self):
        return Entry.objects.filter(pub_dttm__gte=datetime.date.today()-datetime.timedelta(14)).order_by('-pub_dttm', '-id')
    def item_pubdate(self, item):
        return item.get_utc_datetime()

class AtomRecentFeed(RecentFeed):
    feed_type = Atom1Feed
