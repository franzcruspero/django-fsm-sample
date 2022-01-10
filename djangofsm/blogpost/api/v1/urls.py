from django.conf.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from blogpost.api.v1 import viewsets

router = DefaultRouter()
router.register(
    r"",
    viewsets.BlogPostViewSet,
    basename="blogpost",
)

urlpatterns = [
    path(r"", include(router.urls)),
]
