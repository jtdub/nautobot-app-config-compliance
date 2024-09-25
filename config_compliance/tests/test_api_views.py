"""Unit tests for config_compliance."""

from nautobot.apps.testing import APIViewTestCases

from config_compliance import models
from config_compliance.tests import fixtures


class ConfigComplianceModelAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for ConfigComplianceModel."""

    model = models.ConfigComplianceModel
    create_data = [
        {
            "name": "Test Model 1",
            "description": "test description",
        },
        {
            "name": "Test Model 2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_configcompliancemodel()
