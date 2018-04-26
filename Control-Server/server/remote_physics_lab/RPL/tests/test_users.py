from django.test import TestCase
from RPL.models import Users

class UserTestCase(TestCase):
    def setUp(self):
        Users.objects.create(ip="127.0.0.1", place=999)
        
    def test_user_created(self):
        """User was successfully created"""
        
        u1 = Users.objects.get(place=999)
        self.assertEqual(u1.ip, "127.0.0.1")