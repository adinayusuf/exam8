from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.has_perm('change_review'):
            self.object.is_moderate = False
        self.object.save()
        return super().post(request, *args, **kwargs)


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_delete.html'

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={'pk': self.object.product.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avg_mark = sum(Review.objects.filter(product_id=kwargs.get('id')).values_list('mark', flat=True))
        context['average'] = avg_mark
        return context


class ReviewModerateView(PermissionRequiredMixin, View):
    permission_required = 'webapp.change_review'
    def get(self, request, *args, **kwargs):
        qs = Review.objects.filter(is_moderate=False).order_by('-edited_at')
        return render(request, 'review/review_moderate.html', {'reviews': qs})


class ReviewUpdateModerateView(View):
    def get(self, request, *args, **kwargs):
        review_id = kwargs.get('pk')
        r = Review.objects.get(id=review_id)
        r.is_moderate = True
        r.save()
        return redirect('webapp:moderate')
