from .views import UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter  # we can use custom routers


router = SimpleRouter()
router.register('',UserViewSet)

urlpatterns = router.urls

