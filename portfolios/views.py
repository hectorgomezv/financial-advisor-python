from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from portfolios.permissions import IsOwner

from .models import Company, Portfolio, Position
from .serializers import (
    CompanySerializer,
    PortfolioSerializer,
    PositionSerializer,
    UserSerializer,
)


class CompaniesList(APIView):
    """
    List all the companies or creates a new one.
    """

    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompaniesDetail(APIView):
    """
    Retrieve, delete or update a company.
    """

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PortfoliosList(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        user = self.request.user
        return Portfolio.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PortfoliosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsOwner]


class PositionsList(APIView):
    def get(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(id=pk)
            positions = Position.objects.filter(portfolio=portfolio)
            serializer = PositionSerializer(positions, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, pk, format=None):
        serializer = PositionSerializer(data=request.data)
        try:
            if serializer.is_valid():
                user = self.request.user
                company = Company.objects.get(id=request.data["company_id"])
                portfolio = Portfolio.objects.get(id=pk)
                serializer.save(company=company, portfolio=portfolio, owner=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as err:
            return Response(data={"error": str(err)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
