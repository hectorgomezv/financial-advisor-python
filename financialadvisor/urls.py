from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets

from portfolios import views

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('portfolios.urls')),
    path('portfolios/', include('portfolios.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
