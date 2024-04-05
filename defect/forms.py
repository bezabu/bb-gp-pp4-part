from .models import Update, Defect, Category
from cloudinary.forms import CloudinaryFileField
from cloudinary.models import CloudinaryField
from django import forms


class CategoryForm(forms.ModelForm):
    """
    Form class for users to add categories
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Category
        fields = ('name', 'description', 'fa_string', 'colour')


class DefectForm(forms.ModelForm):
    """
    Form class for users to log new defects
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Defect
        fields = ('category', 'title', 'body', 'image_url')


class UpdateForm(forms.ModelForm):
    """
    Form class for users to add new updates
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Update
        fields = ('body', 'image_url', 'resolution')
