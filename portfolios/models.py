from email.policy import default
from pyexpat import model
from django.db import models
from django.forms import FloatField


class Company(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['symbol']


class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('date created')

    def get_assigned_weight(self):
        assigned_weight = 0
        for position in self.position_set.all():
            assigned_weight += position.target_weight
        return assigned_weight

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']


class Position(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    target_weight = models.FloatField()
    shares = models.IntegerField(default=0)

    def __str__(self):
        return self.portfolio.name + ' - ' + self.company.name

    class Meta:
        ordering = ['target_weight']
