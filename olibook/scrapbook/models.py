from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

# Create your models here

class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name='posts', unique=False)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField('Date Published', auto_now_add=True)
    updated = models.DateTimeField('Date Updated', auto_now=True)

    def save(self):
        self.slug = slugify(self.title)
        super(BlogEntry,self).save()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', (), {
            'year': self.pub_date.strftime("%Y"),
            'month': self.pub_date.strftime("%b").lower(),
            'day': self.pub_date.strftime("%d"),
            'slug': self.slug })

    class Meta:
        unique_together = ('author', 'slug')
        get_latest_by = '-created'
