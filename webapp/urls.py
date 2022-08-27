from django.urls import path

from webapp.views.productviews import ProductView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from webapp.views.reviwesview import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', ProductView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail_product'),
    path('produt/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='delete_product'),

    path('product/<int:pk>/review/add/', ReviewCreateView.as_view(), name='review_add'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review_delete')
]
