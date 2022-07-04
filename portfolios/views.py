from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser


from .models import Company
from .serializers import CompanySerializer

# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     # permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def companies_list(request):
    """
    List all the companies or creates a new one.
    """
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def company_detail(request, pk):
    """
    Retrieve, delete or update a company.
    """
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        company.delete()
        return HttpResponse(status=204)


def index(request):
    return HttpResponse("Hi world!")
