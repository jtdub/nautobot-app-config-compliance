"""Models for Config Compliance."""

# Django imports
from django.db import models

# HierConfig imports
from hier_config import text_match

# Nautobot imports
from nautobot.apps.models import PrimaryModel
from nautobot_golden_config.models import ComplianceRule

# from nautobot.apps.models import extras_features
# If you want to use the extras_features decorator please reference the following documentation
# https://docs.nautobot.com/projects/core/en/latest/plugins/development/#using-the-extras_features-decorator-for-graphql
# Then based on your reading you may decide to put the following decorator before the declaration of your class
# @extras_features("custom_fields", "custom_validators", "relationships", "graphql")


# If you want to choose a specific model to overload in your class declaration, please reference the following documentation:
# how to chose a database model: https://docs.nautobot.com/projects/core/en/stable/plugins/development/#database-models

COMPLIANCE_OPERATOR_CHOICES = [
    ("equals", "Equals"),
    ("not_equals", "Not equals"),
    ("startswith", "Starts with"),
    ("endswith", "Ends with"),
    ("contains", "Contains"),
    ("does_not_contain", "Does not contain"),
    ("re_search", "Regex match"),
]
COMPLAINCE_CONDITION_CHOICES = [
    ("and", "AND"),
    ("or", "OR"),
]


class ConfigComplianceModel(PrimaryModel):  # pylint: disable=too-many-ancestors
    """Base model for Config Compliance app."""

    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=512, blank=True)
    golden_config_rule = models.ForeignKey(ComplianceRule, on_delete=models.PROTECT)

    class Meta:
        """Meta class."""

        ordering = ["name"]

        # Option for fixing capitalization (i.e. "Snmp" vs "SNMP")
        # verbose_name = "Config Compliance"

        # Option for fixing plural name (i.e. "Chicken Tenders" vs "Chicken Tendies")
        # verbose_name_plural = "Config Compliances"

    def __str__(self):
        """Stringify instance."""
        return self.name

    def evaluate_chain(self, config):
        """Evaluate the entire chain of rules."""
        for rule_chain_step in self.steps.all():
            result = rule_chain_step.rule.evaluate(config)
            if rule_chain_step.next_step and result:
                rule_chain_step.next_step.evaluate_chain(config)
            elif not result:
                return False
        return True


class ConfigComplianceRuleModel(PrimaryModel):  # pylint: disable=too-many-ancestors
    """Rule model for Config Compliance app."""

    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=512, blank=True)
    operator = models.CharField(max_length=20, choices=COMPLIANCE_OPERATOR_CHOICES)
    config_text = models.TextField()

    def __str__(self):
        """Stringify instance."""
        return self.name

    def evaluate(self, config):
        """Evaluate rule based on provided config text."""
        eval_text = {
            "equals": text_match.equals(config, self.config_text),
            "not_equals": not text_match.equals(config, self.config_text),
            "startswith": text_match.startswith(config, self.config_text),
            "endswith": text_match.endswith(config, self.config_text),
            "contains": text_match.contains(config, self.config_text),
            "does_not_contain": not text_match.contains(config, self.config_text),
            "re_search": text_match.re_search(config, self.config_text),
        }

        return eval_text.get(self.operator)


class ConfigComplianceStepModel(PrimaryModel):  # pylint: disable=too-many-ancestors
    """ConfigComplianceStep model for Config Compliance app."""

    chain = models.ForeignKey(ConfigComplianceModel, on_delete=models.CASCADE)
    rule = models.ForeignKey(ConfigComplianceRuleModel, on_delete=models.CASCADE)
    next_step = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta class."""

        ordering = ["order"]

        # Option for fixing capitalization (i.e. "Snmp" vs "SNMP")
        # verbose_name = "Config Compliance"

        # Option for fixing plural name (i.e. "Chicken Tenders" vs "Chicken Tendies")
        # verbose_name_plural = "Config Compliances"

    def __str__(self):
        """Stringify instance."""
        return f"{self.chain.name} - {self.rule.name} (Step {self.order})"
