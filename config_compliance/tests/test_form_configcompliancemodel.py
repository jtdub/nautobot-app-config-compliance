"""Test configcompliancemodel forms."""

from django.test import TestCase

from config_compliance import forms


class ConfigComplianceModelTest(TestCase):
    """Test ConfigComplianceModel forms."""

    def test_specifying_all_fields_success(self):
        form = forms.ConfigComplianceModelForm(
            data={
                "name": "Development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.ConfigComplianceModelForm(
            data={
                "name": "Development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_configcompliancemodel_is_required(self):
        form = forms.ConfigComplianceModelForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
