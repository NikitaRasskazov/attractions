from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core import views


app_name = 'core'

router = DefaultRouter()
router.register('attractions', views.Attractions)
router.register('categories', views.Category)

urlpatterns = [
    path('', include(router.urls))
]
