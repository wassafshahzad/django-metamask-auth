from django.db import router
from django.urls import path
from rest_framework import routers
from .views import MetaMaskCreateRetrieveViewSet, MetaMaskTokenObtainView


router = routers.SimpleRouter()
router.register(r"metamask", MetaMaskCreateRetrieveViewSet, basename="metamask")


urlpatterns = [
    path(
        "metamask/login/<int:public_address>",
        MetaMaskTokenObtainView.as_view(),
        name="metamask-login",
    )
]

urlpatterns += router.urls
