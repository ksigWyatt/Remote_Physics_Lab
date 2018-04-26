from django.test import TestCase
from RPL.models import Users
from tastypie.test import ResourceTestCaseMixin

class UserTestCase(TestCase):
    def setUp(self):
        Users.objects.create(ip="127.0.0.1", place=999)
        
    def test_user_created(self):
        """User was successfully created"""
        
        u1 = Users.objects.get(place=999)
        self.assertEqual(u1.ip, "127.0.0.1")

    def test_get_queue(self):
        """Testing that the API can return all data from users via GET"""

        resp = self.client.get('/api/queue/', HTTP_HOST='docs.djangoproject.dev:8000')
        self.assertEqual(resp.status_code, 200)