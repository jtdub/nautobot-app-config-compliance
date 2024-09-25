"""API serializers for config_compliance."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from config_compliance import models


class ConfigComplianceModelSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """ConfigComplianceModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.ConfigComplianceModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
