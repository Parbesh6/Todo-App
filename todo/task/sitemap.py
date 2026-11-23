from django.contrib.sitemaps import Sitemap
from models import task

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return task.objects.all()

    def lastmod(self, obj):
        return obj.updated_at