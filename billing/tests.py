from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestBillingAPI(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        pass

    def test_anon_cannot_list_clients(self):
        response = self.client.get(reverse("billing:client-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
