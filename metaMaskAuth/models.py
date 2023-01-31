from django.db import models
from django.contrib.auth import get_user_model
from .utils import generate_random
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class WalletAuthModel(models.Model):
    public_address = models.TextField(primary_key=True, null=False, blank=False)
    nonce = models.TextField(
        default=generate_random,
    )
    user = models.OneToOneField(User, related_name="wallet", on_delete=models.CASCADE)
    nonce_stale = models.BooleanField(default=False)
    refreshed_at = models.DateTimeField(_("Refreshed"), auto_now=True)
