from email.policy import default
from pyexpat import model
from django.db import models
from django.forms import FloatField

class Company(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=6)
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('date created')
    def __str__(self):
        return self.name

class Position(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    target_weight = models.FloatField()
    shares = models.IntegerField(default=0)
    def __str__(self):
        return self.company + ' - ' + self.portfolio