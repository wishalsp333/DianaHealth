from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.http import JsonResponse
from django.db.utils import IntegrityError

class TestSubmitForm(TestCase):
    def test_successful_submission(self):
        data = {
            'email': 'test@example.com',
            'dob': '1990-01-01',
            'age': '18-25',
            'password': 'ValidPassword123@',
        }
        response = self.client.post(reverse('submit_form'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Data successfully inserted!'})

    
    def test_invalid_method(self):
        response = self.client.get(reverse('submit_form'))
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json(), {'message': 'Invalid request.'})
    