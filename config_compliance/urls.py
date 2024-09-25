"""Django urlpatterns declaration for config_compliance app."""

from nautobot.apps.urls import NautobotUIViewSetRouter

from config_compliance import views

router = NautobotUIViewSetRouter()
router.register("custom-compliance", views.ConfigComplianceModelUIViewSet)
router.register("custom-compliance-rules", views.ConfigComplianceRuleModelUIViewSet)

urlpatterns = router.urls
