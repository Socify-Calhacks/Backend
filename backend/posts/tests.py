from django.test import TestCase
from .models import View


class ViewModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        View.objects.create(title='first todo')
        View.objects.create(description='a description here')

    def test_title_content(self):
        view = View.objects.get(id=1)
        expected_object_name = f'{view.title}'
        self.assertEquals(expected_object_name, 'first todo')

    def test_description_content(self):
        view = View.objects.get(id=2)
        expected_object_name = f'{view.description}'
        self.assertEquals(expected_object_name, 'a description here')
# Create your tests here.
