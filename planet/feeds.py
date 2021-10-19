##############################################################################
# Copyright (c) 2010, 2021 Hajime Nakagami <nakagami@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from planet.models import Entry
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
