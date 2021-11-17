from django.urls import path
from product import views

urlpatterns =[
    path('latest-products/', views.LatestProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetails.as_view()),
]