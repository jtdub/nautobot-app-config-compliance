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


class ConfigComplianceRuleModelUIViewSet(NautobotUIViewSet):
    """ViewSet for ConfigComplianceRuleModel views."""

    bulk_update_form_class = forms.ConfigComplianceRuleModelBulkEditForm
    filterset_class = filters.ConfigComplianceRuleModelFilterSet
    filterset_form_class = forms.ConfigComplianceRuleModelFilterForm
    form_class = forms.ConfigComplianceRuleModelForm
    lookup_field = "pk"
    queryset = models.ConfigComplianceRuleModel.objects.all()
    serializer_class = serializers.ConfigComplianceRuleModelSerializer
    table_class = tables.ConfigComplianceRuleModelTable
