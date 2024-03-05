from django import forms
from app.models import donarModel

class addForm(forms.ModelForm):
    class Meta:
        model = donarModel
        fields = '__all__'