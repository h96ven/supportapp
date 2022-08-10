import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_user():
    pass

# class TestGetUsers:
#     def test_if_user_is_anonymous_returns_401(self):
#         client = APIClient()
#         response = client.get('/auth/users/')
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED


# class TestGetUsersMe:
#     def test_if_user_is_anonymous_returns_401(self):
#         client = APIClient()
#         response = client.get('/auth/users/me/')
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED










