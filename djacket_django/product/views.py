from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

# Create your views here.


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetails(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    def get(self, request, category_slug, product_slug):
        product = self.get_object(category_slug, product_slug)
        serializers= ProductSerializer(product)
        return Response(serializers.data)