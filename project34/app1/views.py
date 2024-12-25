from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,TemplateView,DeleteView
from django.urls import reverse,reverse_lazy
from app1.models import Product
# Create your views here.

class IndexView(TemplateView):
    template_name="app1/index.html"
class ProductCreateView(CreateView):
    model=Product
    fields='__all__'
    template_name="app1/create_product.html"
    success_url=reverse_lazy("plist")

class ProductUpdateView(UpdateView):
    model=Product
    fields='__all__'
    template_name="app1/update_product.html"
    success_url=reverse_lazy('ulist')

class ProductListView(ListView):
    model=Product
    fields='__all__'
    template_name="app1/product_update_list.html"
    context_object_name='products'

class ProductDeleteView(DeleteView):
    model=Product
    template_name="app1/prod_conf.html"
    context_object_name='products'
    success_url=reverse_lazy('dlist')

class ProductDeleteListView(ListView):
    model=Product
    fields='__all__'
    template_name="app1/product_delete_list.html"
    context_object_name='products'

class ProductList(ListView):
    model=Product
    fields='__all__'
    template_name="app1/product_list.html"
    context_object_name='products'

