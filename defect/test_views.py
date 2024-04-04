from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import UpdateForm, CategoryForm, DefectForm
from .models import Defect, Category, Update

class TestDefectViews(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.category = Category(name="test category", description="test category description", fa_string="test_fa_string", colour="#TSTCOL")
        self.category.save()
        self.defect = Defect(title="test defect title", category=self.category, author=self.user, body="test defect body", status=0)
        self.defect.save()



    def test_render_category_list_page_with_category_form(self):
        response = self.client.get(reverse('cat_list', args=[]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name="defect/category_list.html")
        self.assertIn(b"test category", response.content)
        #self.assertIn(b"test category description", response.content)
        self.assertIsInstance(
            response.context['category_form'], CategoryForm
        )

    def test_render_log_defect_page_with_defect_form(self):
        response = self.client.get(reverse('log_def', args=[]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name="defect/log_defect.html")
        self.assertIn(b"Log New Defect", response.content)
        self.assertIsInstance(
            response.context['defect_form'], DefectForm
        )

    def test_render_defect_list_page(self):
        response = self.client.get(reverse('def_list', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name="defect/defect_list.html")
        #self.assertIn(b"test defect title", response.content)
        #self.assertIn(b"test defect body", response.content)

    def test_render_defect_detail_page(self):
        response = self.client.get(reverse('def_detail', args=[self.defect.defect_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name="defect/defect_detail.html")
        #self.assertIn(b"test defect title", response.content)
        #self.assertIn(b"test defect body", response.content)
        self.assertIsInstance(
            response.context['update_form'], UpdateForm
        )
