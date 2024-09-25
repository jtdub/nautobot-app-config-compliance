"""App declaration for config_compliance."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class ConfigComplianceConfig(NautobotAppConfig):
    """App configuration for the config_compliance app."""

    name = "config_compliance"
    verbose_name = "Config Compliance"
    version = __version__
    author = "James Williams"
    description = "Config Compliance."
    base_url = "config-compliance"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}


config = ConfigComplianceConfig  # pylint:disable=invalid-name
