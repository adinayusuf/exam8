from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


# Create your views here.
class ProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/index.html'
    ordering = 'category'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail_product.html'
    context_object_name = 'product'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={"pk": self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update_product.html'
    context_object_name = 'product'
    permission_required = 'webapp.update'

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={"pk": self.object.pk})

class ProductDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'webapp.delete'
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('webapp:index')