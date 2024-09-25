"""Test ConfigComplianceModel."""

from django.test import TestCase

from config_compliance import models


class TestConfigComplianceModel(TestCase):
    """Test ConfigComplianceModel."""

    def test_create_configcompliancemodel_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        configcompliancemodel = models.ConfigComplianceModel.objects.create(name="Development")
        self.assertEqual(configcompliancemodel.name, "Development")
        self.assertEqual(configcompliancemodel.description, "")
        self.assertEqual(str(configcompliancemodel), "Development")

    def test_create_configcompliancemodel_all_fields_success(self):
        """Create ConfigComplianceModel with all fields."""
        configcompliancemodel = models.ConfigComplianceModel.objects.create(name="Development", description="Development Test")
        self.assertEqual(configcompliancemodel.name, "Development")
        self.assertEqual(configcompliancemodel.description, "Development Test")
