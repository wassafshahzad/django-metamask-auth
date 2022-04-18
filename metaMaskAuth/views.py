from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import TokenObtainPairSerializer, TokenObtainSlidingSerializer
from .models import WalletAuthModel
from .viewsets import CreateRetrieveViewset
from .api_settings import api_settings


walletAuthSerializer = api_settings.WALLET_AUTHENTICATION_SERIALIZER
token_serializer = (
    TokenObtainSlidingSerializer
    if api_settings.USE_SLIDING_TOKEN
    else TokenObtainPairSerializer
)


class MetaMaskCreateRetrieveViewSet(CreateRetrieveViewset):
    serializer_class = walletAuthSerializer
    queryset = WalletAuthModel.objects.all()


class MetaMaskTokenObtainView(TokenObtainPairView):
    serializer_class = token_serializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["pk"] = self.kwargs.get("public_address")
        return context
