from django.urls import path

from . import views

urlpatterns = [
    path('companies/', views.companies_list),
    path('companies/<int:pk>', views.company_detail),
]
