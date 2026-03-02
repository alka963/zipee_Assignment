from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class TaskTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="1234")
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

    def test_create_task(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post('/api/tasks/', {
            "title": "Test Task",
            "description": "Testing",
            "completed": False
        })
        self.assertEqual(response.status_code, 201)