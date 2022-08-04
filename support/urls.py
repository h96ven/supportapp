from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('tickets', views.TicketViewSet, basename='tickets')

# Two rows of code below are for nested urls like tickets/1/replies/1
tickets_router = routers.NestedDefaultRouter(
                    router, 'tickets', lookup='ticket')

tickets_router.register(
                'replies', views.ReplyViewSet,
                basename='ticket-replies')

urlpatterns = router.urls + tickets_router.urls
