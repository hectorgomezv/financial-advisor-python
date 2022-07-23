from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets

from portfolios import views


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
# router.register(r'companies', views.CompanyViewSet)

base_url = "api/v1/"

urlpatterns = [
    path(base_url + "", include(router.urls)),
    path(base_url + "", include("portfolios.urls")),
    path(base_url + "admin/", admin.site.urls),
    path(
        base_url + "api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
]
