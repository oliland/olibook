from django.db import models
from django.db import signals
from django.db.models.signals import post_save, post_delete
from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from scrapbook.models import BlogEntry

import os
import datetime

stream_models = [
                BlogEntry
                ]


class StreamItem(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    created = models.DateTimeField()
    publisher = models.ForeignKey(User)

    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def get_rendered_html(self):
        # Make sure the object hasn't been deleted
        if self.content_object:
            template_name = 'stream/items/stream_item_%s.html' % (self.content_type.name.replace(' ','_'))
            return render_to_string(template_name, {'object': self.content_object})


def create_stream_item(sender, instance, signal, *args, **kwargs):
    if 'created' in kwargs:
        if kwargs['created']:
            create = True

            ctype = ContentType.objects.get_for_model(instance)

            if ctype.name == "blog entry":
                publisher = instance.author

            created = datetime.datetime.now()

            if create:
                si = StreamItem.objects.get_or_create(content_type=ctype,
                    object_id=instance.id,
                    created=created, publisher=publisher)

def delete_stream_item(sender, instance, signal, *args, **kwargs):
    ctype = ContentType.objects.get_for_model(instance)
    StreamItem.objects.get(content_type=ctype,object_id=instance.id).delete()

for modelname in stream_models:
    post_save.connect(create_stream_item, sender=modelname, dispatch_uid=os.path.dirname(__file__)) # fix for double posting
    post_delete.connect(delete_stream_item, sender=modelname, dispatch_uid=os.path.dirname(__file__))
