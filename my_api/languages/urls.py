from django.urls import path, include
from rest_framework import routers

from .views import LanguageView


router = routers.DefaultRouter()
router.register('languages', LanguageView)

urlpatterns = [
    path('', include(router.urls))
]
