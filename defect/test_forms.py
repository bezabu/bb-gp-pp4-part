from django.test import TestCase
from .forms import DefectForm, UpdateForm, CategoryForm


class TestDefectForm(TestCase):

    def test_form_is_not_valid(self):
        """Test for all fields"""
        defect_form = DefectForm({
            'category': '',
            'title': '',
            'body': '',
        })
        self.assertFalse(defect_form.is_valid(),msg="No data was provided, the form is not valid")

    def test_category_is_not_valid(self):
        """Test for category data type"""
        defect_form = DefectForm({
            'category': 'leak',
            'title': 'test title',
            'body': 'test name of category instead of id',
        })
        self.assertFalse(defect_form.is_valid(),msg="String provided for category instead of integer")

    def test_category_entry_is_not_valid(self):
        """Test for invalid cateogry"""
        defect_form = DefectForm({
            'category': '999',
            'title': 'test title',
            'body': 'body test data',
        })
        self.assertFalse(defect_form.is_valid(),msg="category does not exist")
    
    def test_title_is_not_valid(self):
        """Test for title"""
        defect_form = DefectForm({
            'category': '7',
            'title': '',
            'body': 'body test data',
        })
        self.assertFalse(defect_form.is_valid(),msg="Title data not provided")

    def test_body_is_not_valid(self):
        """Test for body"""
        defect_form = DefectForm({
            'category': '7',
            'title': 'test title',
            'body': '',
        })
        self.assertFalse(defect_form.is_valid(),msg="Body field not provided")



class TestUpdateForm(TestCase):

    def test_update_form_is_valid(self):
        """Test for all fields"""
        update_form = UpdateForm({
            'body': 'This is a great post',
            'resolution': 0,
        })
        self.assertTrue(update_form.is_valid(),msg="All fields provided, form is valid")

    def test_form_is_not_valid(self):
        """Test for body"""
        update_form = UpdateForm({
            'body': '',
            'resolution': 0,
        })
        self.assertFalse(update_form.is_valid(),msg="No body data provided")

    def test_form_is_complete(self):
        """Test for resoltion"""
        update_form = UpdateForm({
            'body': 'body test',
            'resolution': '',
        })
        self.assertFalse(update_form.is_valid(),msg="No resolution data provided")

    def test_form_status_not_valid(self):
        """Test for resolution data type"""
        update_form = UpdateForm({
            'body': 'body test',
            'resolution': 'yes',
        })
        self.assertFalse(update_form.is_valid(),msg="resolution data provided is string, expecting integer")



class TestCategoryForm(TestCase):

    def test_form_empty_not_valid(self):
        """Test for the 'name' field"""
        category_form = CategoryForm({
            'name': '',
            'description': 'short test description',
            'fa_string': 'short_string',
            'colour': '#AAAAAA',
        })
        self.assertFalse(category_form.is_valid(),msg="Name was not provided")
    
    def test_form_empty_not_valid(self):
        """Test for the 'description' field"""
        category_form = CategoryForm({
            'name': 'name',
            'description': '',
            'fa_string': 'short_string',
            'colour': '#AAAAAA',
        })
        self.assertFalse(category_form.is_valid(),msg="Description was not provided")

    def test_category_form_is_valid(self):
        """Test for the 'fa_string' field"""
        category_form = CategoryForm({
            'name': 'name',
            'description': 'short test description',
            'fa_string': '',
            'colour': '#AAAAAA',
        })
        self.assertFalse(category_form.is_valid(),msg="fa_string was not provided")

    def test_form_is_valid(self):
        """Test for the 'colour' field"""
        category_form = CategoryForm({
            'name': 'name',
            'description': 'short test description',
            'fa_string': 'fa_string',
            'colour': '',
        })
        self.assertFalse(category_form.is_valid(),msg="Colour was not provided")

    def test_form_is_valid(self):
        """Test for all fields"""
        category_form = CategoryForm({
            'name': 'name',
            'description': 'short test description',
            'fa_string': 'short_string',
            'colour': '#AAAAAA',
        })
        self.assertTrue(category_form.is_valid(),msg="All fields provided")

    def test_form_colour_is_not_valid(self):
        """Test for colour max length"""
        category_form = CategoryForm({
            'name': 'name',
            'description': 'short test description',
            'fa_string': 'short_string',
            'colour': 'toomanycharacters',
        })
        self.assertFalse(category_form.is_valid(),msg="The data provided for colour was too long")

    def test_form_fa_string_is_not_slug(self):
        """Test for spaces in fa_string"""
        category_form = CategoryForm({
            'name': 'name',
            'description': 'short test description',
            'fa_string': 'short string with spaces',
            'colour': '123456',
        })
        self.assertFalse(category_form.is_valid(),msg="The data provided for fa_string included characters not allowed in a slug")

    def test_form_name_length_is_not_valid(self):
        """Test for name max length"""
        category_form = CategoryForm({
            'name': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum.',
            'description': 'short test description',
            'fa_string': 'short_string',
            'colour': '123456',
        })
        self.assertFalse(category_form.is_valid(),msg="The data provided for name was too long")

    def test_form_fa_string_too_long_is_not_valid(self):
        """Test for fa_string length"""
        category_form = CategoryForm({
            'name': 'name',
            'description': 'short test description',
            'fa_string': 'dfadfdfgbvkdufgbkvd-gfbkdvfgbdufgnkvsdfhncsdfhguv-sbgdifugnscdgfdugfvbksdugflac_nkjdhfcgauydgfcbassud',
            'colour': '123456',
        })
        self.assertFalse(category_form.is_valid(),msg="The data provided for fa_string was too long")

    