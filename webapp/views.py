from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

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

    # def get_context_data(self, **kwargs):
    #     contex = super().get_context_data(**kwargs)
    #     product = self.get_object()
    #     contex['average'] = product.get_average_mark()
    #     return contex


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


