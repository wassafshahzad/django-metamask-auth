from django.contrib.auth import get_user_model, hashers
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken

from .utils import verify_singature
from .models import WalletAuthModel
from .api_settings import api_settings

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [*User.REQUIRED_FIELDS, "username"]

    def create(self, validated_data):
        validated_data["password"] = hashers.make_password(None)
        return super().create(validated_data)


class WalletAuthSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=False)

    def create(self, validated_data):
        user = validated_data.pop("user")
        user = User.objects.create(**user, password=hashers.make_password(None))
        wallet = WalletAuthModel.objects.create(**validated_data, user=user)
        return wallet

    class Meta:
        model = WalletAuthModel
        fields = ["public_address", "nonce", "user"]
        read_only_fields = ["nonce"]
        extra_kwargs = {"user": {"wite_only": True}}


## Same as TokenObtainSerializer with a diffrent validation function
## Tech dept: make signature field dynamicaly from settings
class WalletTokenObtainSerializer(serializers.Serializer):
    token_class = None
    signature = serializers.CharField(max_length=200)

    def validate(self, attrs):
        try:
            pk = self.context["pk"]
        except KeyError:
            raise KeyError("Id must be passed in context")
        wallet = get_object_or_404(WalletAuthModel, pk=pk)
        signature = attrs["signature"]
        if verify_singature(wallet.nonce, signature):
            self.user = wallet.user
        return {}

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)


## Same as TokaneObtainPairSerializer from simple-jwt but diffrent base class
class TokenObtainPairSerializer(WalletTokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class TokenObtainSlidingSerializer(WalletTokenObtainSerializer):
    token_class = SlidingToken

    def validate(self, attrs):
        data = super().validate(attrs)

        token = self.get_token(self.user)

        data["token"] = str(token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return
