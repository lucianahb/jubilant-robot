from django.shortcuts import render
from .serializers import SellerSerializer
from .models import Seller
from rest_framework import viewsets


class SellerViewSet(viewset.ModelViewSet):
    queryset = Seller.objects.all().order_by('name')
    serializer_class = SellerSerializer
