from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("companies/", views.CompaniesList.as_view()),
    path("companies/<int:pk>", views.CompaniesDetail.as_view()),
    path("portfolios/", views.PortfoliosList.as_view()),
    path("portfolios/<int:pk>", views.PortfoliosDetail.as_view()),
    path("portfolios/<int:pk>/positions", views.PositionsList.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
