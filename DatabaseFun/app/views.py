"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
def artistdetails(request, id):
    artist = Artist.objects.get(pk = id)
    return render_to_response('app/artistdetails.html',{'artist':artist})
    #output = '<html><head><title>' + name
    #output += '</title></head><body><h1>'+name+'</h1></body></html>'
    #return HttpResponse(output);

def artists(request):
    artists = Artist.objects.all()
    return render_to_response('app/artists.html',{'artists':artists})
    #return HttpResponse('<html><head><title>Hello, Django</title></head><body><h1>Hello, Django</h1></body></html>')

def artistcreate(request):
    if request.method == "GET":
        form = ArtistForm()
        return render(request,'app/create.html',{ 'form':form })
    elif request.method == "POST":
        form = ArtistForm(request.POST)
        form.save()
        return HttpResponseRedirect('/artists')