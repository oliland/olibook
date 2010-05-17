# RAMIREZ! Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from stream.models import *

def stream(request):
    stream = StreamItem.objects.all().order_by('-created')
    return render_to_response('stream/base.html',
            { 'stream': stream }, context_instance=RequestContext(request))
