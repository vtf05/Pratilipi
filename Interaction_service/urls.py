from .views import LikeViewSet , ReadViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter  # we can use custom routers


router = SimpleRouter()
router.register('like', LikeViewSet)
router.register('read', ReadViewSet)
urlpatterns = router.urls

