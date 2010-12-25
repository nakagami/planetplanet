##############################################################################
# Copyright (c) 2010 Hajime Nakagami <nakagami@gmail.com>
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
from django.db import models
from django.conf import settings
import datetime
from dateutil import zoneinfo, tz

class Feed(models.Model):
    rss_url = models.CharField(max_length=1024)
    title = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=1024, blank=True)
    subtitle = models.CharField(max_length=2048, blank=True)
    author = models.CharField(max_length=200, blank=True)
    pub_dttm_offset = models.IntegerField(default=0, blank=True)
    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.rss_url

class Entry(models.Model):
    link = models.CharField(max_length=1024)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200, blank=True)
    pub_dttm = models.DateTimeField()
    feed = models.ForeignKey(Feed)
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.link

    def get_utc_datetime(self):
        t = self.pub_dttm.timetuple()
        return datetime.datetime(t[0], t[1], t[2], t[3], t[4], t[5], t[6], tz.tzutc())

    def get_local_datetime(self):
        return self.pub_dttm.replace(tzinfo=tz.tzutc()).astimezone(zoneinfo.gettz(settings.TIME_ZONE))

    def pub_date(self):
        return self.get_local_datetime().date()

    def pub_time(self):
        t = self.get_local_datetime().time()
        return datetime.time(t.hour, t.minute, t.second)
