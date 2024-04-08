from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from .models import ShopCard
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from taggit.models import Tag


class ShopProducts(ListView):
    model = ShopCard
    context_object_name = 'cards'

def index(request):
    return render(request, "shop/index.html")

def contact(request):
    return render(request, "shop/contact.html")
def blog_list(request):
    return render(request, "shop/blog_list.html")
def product(request):
    return render(request, "shop/product.html")
def about(request):
    return render(request, "shop/about.html")
def testimonial(request):
    return render(request, "shop/testimonial.html")
