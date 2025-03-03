from django import forms
from .models import Barcode

class BarcodeUploadForm(forms.ModelForm):
    class Meta:
        model = Barcode
        fields = ['image']
