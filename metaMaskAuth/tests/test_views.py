from parameterized import parameterized
from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class WalletCreateRetrieveTest(APITestCase):
    def setUp(self) -> None:
        User.objects.create(username="already_exist")

    @parameterized.expand(
        [
            (
                {
                    "user": {
                        "username": "test1",
                    },
                    "public_address": "1231#!@312jbwi12y3br",
                },
                status.HTTP_201_CREATED,
            ),
            (
                {
                    "user": {
                        "username": "test1",
                    },
                },
                status.HTTP_400_BAD_REQUEST,
            ),
            (
                {
                    "user": {
                        "email": "test@gmail.com",
                    },
                    "public_address": "1231#!@312jbwi12y3adasd",
                },
                status.HTTP_400_BAD_REQUEST,
            ),
            (
                {
                    "user": {
                        "username": "already_exist",
                    },
                    "public_address": "1231#!@312jbwi12y3br",
                },
                status.HTTP_400_BAD_REQUEST,
            ),
        ]
    )
    def test_create_wallet(self, data, expected):
        url = reverse("metamask-list")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, expected)
