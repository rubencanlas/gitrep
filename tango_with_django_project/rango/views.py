# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! <a href='/rango/about/'>About Rango</a>")
    
def about(request):
    return HttpResponse("About page. <a href='/rango/'>Back to index</a>")