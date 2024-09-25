"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from config_compliance import models
from config_compliance.tests import fixtures


class ConfigComplianceModelViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the ConfigComplianceModel views."""

    model = models.ConfigComplianceModel
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }
    csv_data = (
        "name",
        "Test csv1",
        "Test csv2",
        "Test csv3",
    )

    @classmethod
    def setUpTestData(cls):
        fixtures.create_configcompliancemodel()
