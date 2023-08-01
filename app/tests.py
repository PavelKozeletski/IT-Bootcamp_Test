from django.test import TestCase
from django.urls import reverse
from .models import Author

class AuthorCreationTest(TestCase):
    def test_author_creation(self):
        author_data = {'name': 'Test Author'}
        response = self.client.post(reverse('input_author'), data=author_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Author.objects.filter(name='Test Author').exists())