from .models import Update, Defect, Category
from cloudinary.forms import CloudinaryFileField
from cloudinary.models import CloudinaryField
from django import forms


class UpdateForm(forms.ModelForm):
    #image = CloudinaryFileField()
    class Meta:
        model = Update
        fields = ('body', 'image_url', 'resolution')
    

        

class DefectForm(forms.ModelForm):
    #image_url = CloudinaryFileField()
    class Meta:
        model = Defect
        fields = ('category', 'title', 'body', 'image_url')
        #fields = ('category', 'title', 'body')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', 'fa_string', 'colour')