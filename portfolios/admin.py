from django.contrib import admin

from .models import Company, Portfolio, Position

admin.site.register(Company)
admin.site.register(Portfolio)
admin.site.register(Position)
