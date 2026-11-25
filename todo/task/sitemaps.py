from django.contrib.sitemaps import Sitemap
from .models import task

class TaskSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return task.objects.all()


class PageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['home']  # Add other static pages if needed

    def location(self, item):
        from django.urls import reverse
        return reverse(item)