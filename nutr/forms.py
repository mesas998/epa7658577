from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import HiddenInput
from .models import NutrDef, NutData

class NutrDefForm (forms.ModelForm):
    class Meta:
        model = NutrDef
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()

class NutrDefForm(forms.ModelForm):
    class Meta:
        model = NutrDef
        fields = '__all__'

class NutDataForm(forms.ModelForm):
    class Meta:
        model = NutData
        fields = '__all__'
