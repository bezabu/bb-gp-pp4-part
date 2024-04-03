from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import UpdateForm, CategoryForm
from .models import Defect, Category

class TestDefectViews(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.category = Category(name="test category", description="test category description", fa_string="test_fa_string", colour="#TSTCOL")
        self.category.save()
        self.defect = Defect(defect_id=1, title="test defect title", category=self.category, author=self.user, body="test defect body")
        self.defect.save()

    def test_render_category_list_page_with_category_form(self):
        response = self.client.get(reverse('cat_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test category", response.content)
        self.assertIn(b"test category description", response.content)
        self.assertIsInstance(
            response.context['category_form', CategoryForm]
        )

    def test_render_defect_list_page(self):
        response = self.client.get(reverse('def_list', args=['1']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test defect title", response.content)
        self.assertIn(b"test defect body", response.content)
        

