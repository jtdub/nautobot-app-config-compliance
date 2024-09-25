"""API views for config_compliance."""

from nautobot.apps.api import NautobotModelViewSet

from config_compliance import filters, models
from config_compliance.api import serializers


class ConfigComplianceModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """ConfigComplianceModel viewset."""

    queryset = models.ConfigComplianceModel.objects.all()
    serializer_class = serializers.ConfigComplianceModelSerializer
    filterset_class = filters.ConfigComplianceModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
