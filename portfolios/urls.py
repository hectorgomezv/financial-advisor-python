from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('companies/', views.CompaniesList.as_view()),
    path('companies/<int:pk>', views.CompaniesDetail.as_view()),
    path('portfolios/', views.PortfoliosList.as_view()),
    path('portfolios/<int:pk>', views.PortfoliosDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
