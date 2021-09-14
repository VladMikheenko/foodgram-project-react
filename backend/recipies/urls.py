from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('recipies', views.RecipeViewSet)
urlpatterns = router.urls
