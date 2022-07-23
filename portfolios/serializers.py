from django.contrib.auth.models import User
from .models import Company, Portfolio, Position
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "symbol"]


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Portfolio
        fields = ["id", "name", "created", "owner"]


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Position
        fields = [
            "id",
            "target_weight",
            "shares",
            "company_id",
            "portfolio_id",
            "owner",
        ]


class UserSerializer(serializers.ModelSerializer):
    portfolios = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Portfolio.objects.all()
    )
    positions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Position.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "portfolios"]
