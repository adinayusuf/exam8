from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Product, Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'review/review_create.html'
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        user = self.request.user
        form.instance.product = product
        form.instance.author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={'pk': self.object.product.pk})


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/update_review.html'

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_delete.html'

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={'pk': self.object.product.pk})
