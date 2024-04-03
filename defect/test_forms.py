from django.test import TestCase
from .forms import DefectForm, UpdateForm

#fields = ('category', 'title', 'body', 'image_url')

class TestDefectForm(TestCase):

    def test_form_is_not_valid(self):
        defect_form = DefectForm({
            'category': '',
            'title': '',
            'body': '',
        })
        self.assertFalse(defect_form.is_valid())

    def test_form_is_valid(self):
        defect_form = DefectForm({
            'category': '3',
            'title': 'test title',
            'body': 'test body',
        })
        self.assertFalse(defect_form.is_valid())


class TestUpdateForm(TestCase):

    def test_form_is_valid(self):
        update_form = UpdateForm({
            'body': 'This is a great post',
            'resolution': 0,
        })
        self.assertTrue(update_form.is_valid())

    def test_form_is_not_valid(self):
        update_form = UpdateForm({
            'body': '',
            'resolution': 0,
        })
        self.assertFalse(update_form.is_valid())

    def test_form_is_complete(self):
        update_form = UpdateForm({
            'body': '',
            'resolution': '',
        })
        self.assertFalse(update_form.is_valid())

    def test_form_status_not_valid(self):
        update_form = UpdateForm({
            'body': '',
            'resolution': 'yes',
        })
        self.assertFalse(update_form.is_valid())