"""Views for config_compliance."""

from nautobot.apps.views import NautobotUIViewSet

from config_compliance import filters, forms, models, tables
from config_compliance.api import serializers


class ConfigComplianceModelUIViewSet(NautobotUIViewSet):
    """ViewSet for ConfigComplianceModel views."""

    bulk_update_form_class = forms.ConfigComplianceModelBulkEditForm
    filterset_class = filters.ConfigComplianceModelFilterSet
    filterset_form_class = forms.ConfigComplianceModelFilterForm
    form_class = forms.ConfigComplianceModelForm
    lookup_field = "pk"
    queryset = models.ConfigComplianceModel.objects.all()
    serializer_class = serializers.ConfigComplianceModelSerializer
    table_class = tables.ConfigComplianceModelTable
