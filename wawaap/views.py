from django.shortcuts import render
from .forms import Userform
from .models import User, Websites
# Create your views here.


def home(request):
     return render(request, 'wawaap/home.html') 

def gallery(request):
     type = Websites.objects.filter(type="Latest")
     all = Websites.objects.filter(type="Business")
     store = Websites.objects.filter(type="E-commerce")
     apps = Websites.objects.filter(type="Webapp")
     art = Websites.objects.filter(type="Artistic")
     nav = Websites.objects.all()
     context = {"type": type, "all":all, "store":store, "apps":apps, "art":art, "nav":nav}
     return render(request, 'wawaap/gallery.html', context) 

def about(request):
     return render(request, 'wawaap/about.html') 

def contact(request):
     form = Userform(request.POST or None)
     if form.is_valid():
        form.save()
        form = Userform()
     context = { "form": form }
     return render(request, 'wawaap/contact.html', context) 
 
def price(request):
     return render(request, 'wawaap/price.html') 
     



def business(request):
     all = Websites.objects.filter(type="Business")
     context = {"all":all}
     return render(request, 'wawaap/business.html', context) 


def commerce(request):
     store = Websites.objects.filter(type="E-commerce")
     context = {"store":store}
     return render(request, 'wawaap/commerce.html', context) 

def art(request):
     art = Websites.objects.filter(type="Artistic")
     context = {"art":art}
     return render(request, 'wawaap/art.html', context) 

def webapp(request):
     apps = Websites.objects.filter(type="Webapp")
     context = {"apps":apps}
     return render(request, 'wawaap/webapp.html', context) 
