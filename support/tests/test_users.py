import pytest
from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
class TestPostUser:
    def test_if_register_user_returns_201(self):
        payload = dict(
            username='user7',
            email='user7@domain.com',
            password='ILoveDjango'
        )

        response = client.post('/auth/users/', payload)
        assert response.status_code == status.HTTP_201_CREATED

    def test_if_login_user_returns_200(self):
        payload = dict(
            username='user7',
            email='user7@domain.com',
            password='ILoveDjango'
        )

        client.post('/auth/users/', payload)

        response = client.post('/auth/jwt/create/',
                               dict(username='user7',
                                    password='ILoveDjango'))

        assert response.status_code == status.HTTP_200_OK

    def test_if_login_user_with_wrong_credentials_returns_401(self):
        response = client.post('/auth/jwt/create/',
                               dict(username='user1001',
                                    password='whfebgwuhfdevbgu'))

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestGetUsers:
    def test_if_user_is_anonymous_returns_401(self):
        response = client.get('/auth/users/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
