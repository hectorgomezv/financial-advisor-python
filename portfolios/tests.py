from django.test import TestCase
from django.utils import timezone

from .models import Company, Portfolio, Position

class PortfolioModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_company = Company(name='Test company', symbol='TST')
        cls.test_company.save()
        cls.another_test_company = Company(name='Another test company', symbol='TST2')
        cls.another_test_company.save()
        cls.portfolio = Portfolio(name='Test Portfolio', created=timezone.now())
        cls.portfolio.save()

    def test_get_assigned_weight_with_no_positions(self):
        """
        get_assigned_weight() returns 0 when there's no positions
        """
        portfolio = Portfolio(name='Test Portfolio', created=timezone.now())
        self.assertEqual(portfolio.get_assigned_weight(), 0)

    def test_get_assigned_weight_with_one_position(self):
        """
        get_assigned_weight() returns the position weight when there's one position
        """
        position = Position(company=self.test_company, portfolio=self.portfolio, target_weight=52, shares=2)
        position.save()
        self.assertEqual(self.portfolio.get_assigned_weight(), 52)

    def test_get_assigned_weight_with_several_positions(self):
        """
        get_assigned_weight() returns the position weight when there's one position
        """
        position = Position(company=self.test_company, portfolio=self.portfolio, target_weight=52, shares=2)
        position.save()
        position = Position(company=self.another_test_company, portfolio=self.portfolio, target_weight=18, shares=2)
        position.save()
        self.assertEqual(self.portfolio.get_assigned_weight(), 70)

