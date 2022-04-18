from django.conf import settings
from django.test.signals import setting_changed
from rest_framework.settings import APISettings

DEFAULTS = {
    "UPDATE_LAST_LOGIN": False,
    "NONCE_LEN": 24,
    "VALIDATION_SERIALIZER": "metaMaskAuth.serializers.WalletTokenObtainSerializer",
    "WALLET_AUTHENTICATION_SERIALIZER": "metaMaskAuth.serializers.WalletAuthSerializer",
    "USE_SLIDING_TOKEN": False,
}

STRING_IMPORTS = [
    "VALIDATION_SERIALIZER",
    "WALLET_AUTHENTICATION_SERIALIZER",
]

USER_SETTINGS = getattr(settings, "METAMASK_AUTH", {})


api_settings = APISettings(USER_SETTINGS, DEFAULTS, STRING_IMPORTS)


def reload_api_settings(*args, **kwargs):
    global api_settings

    setting, value = kwargs["setting"], kwargs["value"]

    if setting == "METAMASK_AUTH":
        api_settings = APISettings(value, DEFAULTS)


setting_changed.connect(reload_api_settings)
