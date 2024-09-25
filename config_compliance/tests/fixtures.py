"""Create fixtures for tests."""

from config_compliance.models import ConfigComplianceModel


def create_configcompliancemodel():
    """Fixture to create necessary number of ConfigComplianceModel for tests."""
    ConfigComplianceModel.objects.create(name="Test One")
    ConfigComplianceModel.objects.create(name="Test Two")
    ConfigComplianceModel.objects.create(name="Test Three")
