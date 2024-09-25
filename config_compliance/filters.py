"""Filtering for config_compliance."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from config_compliance import models


class ConfigComplianceModelFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for ConfigComplianceModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.ConfigComplianceModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]


class ConfigComplianceRuleModelFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for ConfigComplianceRuleModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.ConfigComplianceRuleModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description", "config_text"]
