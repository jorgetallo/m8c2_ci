from django.test import TestCase, Client

# Create your tests here.
class HomeTests(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_endpoint_home_responde_grupo3(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"Grupo": "3"})
