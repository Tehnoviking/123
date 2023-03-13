

from ..models import Category
from django.urls import reverse
from django.test import TestCase

class TestCategoriesView(TestCase):
    fixtures = ["api/tests/fixtures/fixtures_categories.json",]


    def test_categories_all_view(self):
        response = self.client.get(reverse('categories-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data,[
            {
                "id":1,
                "name":"categories1",
                "description":"some description"
            }
        ])
