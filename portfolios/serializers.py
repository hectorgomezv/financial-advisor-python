from django.contrib.auth.models import User
from .models import Company, Portfolio, Position
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "symbol"]


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    companyName = serializers.SerializerMethodField()
    symbol = serializers.SerializerMethodField()

    def get_companyName(self, obj):
        return obj.company.name

    def get_symbol(self, obj):
        return obj.company.symbol

    class Meta:
        model = Position
        fields = [
            "id",
            "target_weight",
            "shares",
            "company_id",
            "companyName",
            "symbol",
            "portfolio_id",
            "owner",
        ]


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    positions = PositionSerializer(many=True)

    class Meta:
        model = Portfolio
        fields = ["id", "name", "created", "owner", "positions"]


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
