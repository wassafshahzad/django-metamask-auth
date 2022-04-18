from django.db import router
from django.urls import path
from rest_framework import routers
from .views import MetaMaskCreateRetrieveViewSet, MetaMaskTokenObtainView


router = routers.SimpleRouter()
router.register(r"", MetaMaskCreateRetrieveViewSet, basename="metamask")


urlpatterns = [
    path(
        "login/<str:public_address>",
        MetaMaskTokenObtainView.as_view(),
        name="metamask-login",
    )
]

urlpatterns += router.urls
