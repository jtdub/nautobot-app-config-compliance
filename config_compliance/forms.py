"""Forms for config_compliance."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from config_compliance import models


class ConfigComplianceModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """ConfigComplianceModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.ConfigComplianceModel
        fields = [
            "name",
            "description",
        ]


class ConfigComplianceModelBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """ConfigComplianceModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.ConfigComplianceModel.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class ConfigComplianceModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.ConfigComplianceModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
