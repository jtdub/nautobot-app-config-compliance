"""Test ConfigComplianceModel Filter."""

from django.test import TestCase

from config_compliance import filters, models
from config_compliance.tests import fixtures


class ConfigComplianceModelFilterTestCase(TestCase):
    """ConfigComplianceModel Filter Test Case."""

    queryset = models.ConfigComplianceModel.objects.all()
    filterset = filters.ConfigComplianceModelFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for ConfigComplianceModel Model."""
        fixtures.create_configcompliancemodel()

    def test_q_search_name(self):
        """Test using Q search with name of ConfigComplianceModel."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for ConfigComplianceModel."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
