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
