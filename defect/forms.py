from .models import Update, Defect
from django import forms


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ('body','resolution',)

class DefectForm(forms.ModelForm):
    class Meta:
        model = Defect
        fields = ('category', 'title', 'body')