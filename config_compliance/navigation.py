"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:config_compliance:configcompliancemodel_list",
        name="Config Compliance",
        permissions=["config_compliance.view_configcompliancemodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:config_compliance:configcompliancemodel_add",
                permissions=["config_compliance.add_configcompliancemodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Config Compliance", items=tuple(items)),),
    ),
)
