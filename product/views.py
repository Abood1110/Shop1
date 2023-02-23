from django.views.generic import View , TemplateView ,ListView , DetailView
#from django.shortcuts import render
from .models import Product


class HomeView(ListView):
    # def get(self,request,*args, **kwargs):
    #     return render(request,'home.html')

    template_name= 'home.html'
    model = Product
    context_object_name= "products"


class ProductDetailView(DetailView):
    template_name = 'detail.html'
    model = Product
    context_object_name = "product"