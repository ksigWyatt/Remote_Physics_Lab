from django.test import TestCase
from RPL.models import Rpl
from tastypie.test import ResourceTestCaseMixin, TestApiClient

class VarsTestCase(ResourceTestCaseMixin, TestCase):
    def setUp(self):
        Rpl.objects.create(variables="accelv", values=0, currentvalue=0)
        Rpl.objects.create(variables="current", values=0, currentvalue=1.0)
        
    def test_var_created(self):
        """Var was successfully created"""
        
        r1 = Rpl.objects.get(variables="accelv")
        self.assertEqual(r1.values, 0)

    def test_current_has_value(self):
        """Current has value for current-value"""
        
        r2 = Rpl.objects.get(variables="current")
        self.assertEqual(r2.currentvalue, 1.0)

    def test_get_vars(self):
        """Testing that the API can return all data from vars via GET"""

        resp = self.client.get('/api/variables/', HTTP_HOST='docs.djangoproject.dev:8000')
        self.assertEqual(resp.status_code, 200)

    def test_put_vars(self):
        """ Performs PUT request for vars id=1"""
        client = TestApiClient()

        response = client.put('/api/variables/1/', data={
            'values': 150
        })

        # 204 == Action Performed -> No Data
        self.assertEqual(response.status_code, 204)

    def test_put_vars_for_current(self):
        """ Performs PUT request for currentvalue of id=2"""
        client = TestApiClient()

        response = client.put('/api/variables/2/', data={
            'currentvalue': 2.15
        })

        # 204 == Action Performed -> No Data
        self.assertEqual(response.status_code, 204)