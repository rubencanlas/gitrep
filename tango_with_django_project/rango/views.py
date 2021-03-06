# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for eg.
    context = RequestContext(request)
    
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template.
    context_dict = {'boldmessage': "I am bold font from the context"}
    
    # Return a rendered response to send to the client.
    # We make use of a shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('rango/index.html', context_dict, context)
    
    #return HttpResponse("Hello, world! <a href='/rango/about/'>About Rango</a>")
    
def about(request):
    context = RequestContext(request)
    context_dict = {'aboutmessage': "This is the about message in context_dic. "}
    return render_to_response('rango/about.html', context_dict, context)

    
    #return HttpResponse("About page. <a href='/rango/'>Back to index</a>")