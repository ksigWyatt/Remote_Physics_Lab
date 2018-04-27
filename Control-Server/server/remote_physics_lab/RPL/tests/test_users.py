from django.test import TestCase
from RPL.models import Users
from tastypie.test import ResourceTestCaseMixin, TestApiClient

class UserTestCase(TestCase):
    def setUp(self):
        Users.objects.create(ip="127.0.0.1", place=999)
        Users.objects.create(ip="127.0.0.1", place=998)
        
    def test_user_created(self):
        """ User was successfully created """
        
        u1 = Users.objects.get(place=999)
        self.assertEqual(u1.ip, "127.0.0.1")

    def test_get_queue(self):
        """ Testing that the API can return all data from users via GET """

        resp = self.client.get('/api/queue/', HTTP_HOST='docs.djangoproject.dev:8000')
        self.assertEqual(resp.status_code, 200)

    def test_post_queue(self):
        """ Performs POST request to queue """
        client = TestApiClient()

        response = client.post('/api/queue/', data={
            'ip': '127.0.0.1',
            'place': 997
        })

        # 201 == Created
        self.assertEqual(response.status_code, 201)

    def test_put_queue(self):
        """ Performs PUT request for queue id=1"""
        client = TestApiClient()

        response = client.put('/api/queue/2/', data={
            'place': 990
        })

        # 204 == Action Performed -> No Data
        self.assertEqual(response.status_code, 204)

    def test_delete_queue_item(self):
        """ Performs DELETE request to queue id 1"""
        client = TestApiClient()

        response = client.delete('/api/queue/2/',data={'format': 'json'})

        # 204 == Action Performed -> No Data
        self.assertEqual(response.status_code, 204)
