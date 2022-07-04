from math import perm
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions

from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-name')
    serializer_class = CompanySerializer
    # permission_classes = [permissions.IsAuthenticated]

def index(request):
    return HttpResponse("Hi world!")
