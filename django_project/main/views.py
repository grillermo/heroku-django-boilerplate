from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.conf import settings

def generic_view(request,context={},template_name=None): 
    return render_to_response(template_name,context,context_instance=RequestContext(request))

