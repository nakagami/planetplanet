from planetplanet.planet.models import Feed, Entry
from django.contrib import admin

class FeedAdmin(admin.ModelAdmin):
    fields = ['rss_url', 'pub_dttm_offset']

admin.site.register(Feed, FeedAdmin)
