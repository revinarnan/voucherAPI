from django.shortcuts import render
from rest_framework import viewsets

from .serializers import VouchersSerializers
from .models import Vouchers

# Create your views here.
class VouchersViewSet(viewsets.ModelViewSet):
    queryset = Vouchers.objects.all().order_by('kota')
    serializer_class = VouchersSerializers
