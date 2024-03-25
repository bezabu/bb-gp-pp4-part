from .models import Update, Defect, Category
from django import forms


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ('body','resolution',)

class DefectForm(forms.ModelForm):
    class Meta:
        model = Defect
        fields = ('category', 'title', 'body')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', 'fa_string', 'colour')