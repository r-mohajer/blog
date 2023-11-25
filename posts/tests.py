from django.contrib.auth.models import User
from django.test import TestCase
from factory.django import DjangoModelFactory
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User


class TestPostViewSet(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            "john", "lennon@thebeatles.com", "johnpassword"
        )
        self.api_client = APIClient()

    def test_create_post(self):
        self.api_client.login(username="john", password="johnpassword")
        url = reverse("posts-list")
        data = {
            "title": "sample post",
            "content": "sample context",
        }

        response = self.api_client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_create_post_fail(self):
        url = reverse("posts-list")
        data = {
            "title": "sample post",
            "content": "sample context",
        }

        response = self.api_client.post(url, data, format="json")
        self.assertEqual(response.status_code, 403)
