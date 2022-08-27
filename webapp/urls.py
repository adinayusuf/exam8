from django.urls import path

from webapp.views import ProductView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', ProductView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail_product'),
    path('produt/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
]
