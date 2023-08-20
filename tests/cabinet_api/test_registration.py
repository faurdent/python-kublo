import json

from django.shortcuts import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class TestRegistration(APITestCase):
    def test_valid_registration(self):
        registration_data = {
            "email": "test@example.com",
            "password": "testpassword",
            "password2": "testpassword",
        }
        response = self.client.post(reverse("register"), data=registration_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        response_data = json.loads(response.content)
        assert "access" in response_data and "refresh" in response_data

    def test_invalid_registration(self):
        registration_data_email_invalid = {
            "email": "testexample.com",
            "password": "testpassword",
            "password2": "testpassword",
        }
        response = self.client.post(reverse("register"), data=registration_data_email_invalid, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        response_data = json.loads(response.content)
        assert "email" in response_data

        registration_data_passwords_invalid = {
            "email": "test@example.com",
            "password": "testpassword",
            "password2": "testpassword1234",
        }
        response = self.client.post(reverse("register"), data=registration_data_passwords_invalid, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        response_data = json.loads(response.content)
        assert "password2" in response_data
