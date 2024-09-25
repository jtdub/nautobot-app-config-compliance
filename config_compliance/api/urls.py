"""Django API urlpatterns declaration for config_compliance app."""

from nautobot.apps.api import OrderedDefaultRouter

from config_compliance.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("configcompliancemodel", views.ConfigComplianceModelViewSet)

urlpatterns = router.urls
