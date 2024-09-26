"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:config_compliance:configcompliancemodel_list",
        name="Compliance Chain",
        permissions=["config_compliance.view_configcompliancemodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:config_compliance:configcompliancemodel_add",
                permissions=["config_compliance.add_configcompliancemodel"],
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:config_compliance:configcompliancerulemodel_list",
        name="Compliance Rules",
        permissions=["config_compliance.view_configcompliancerulemodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:config_compliance:configcompliancerulemodel_add",
                permissions=["config_compliance.add_configcompliancerulemodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Golden Config",
        groups=(NavMenuGroup(name="Custom Compliance", items=tuple(items)),),
    ),
)
