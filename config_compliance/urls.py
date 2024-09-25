"""Django urlpatterns declaration for config_compliance app."""

from nautobot.apps.urls import NautobotUIViewSetRouter

from config_compliance import views

router = NautobotUIViewSetRouter()
router.register("configcompliancemodel", views.ConfigComplianceModelUIViewSet)

urlpatterns = router.urls
