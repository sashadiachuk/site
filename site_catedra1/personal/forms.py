from django import forms
from .models import * #з файла моделс імпортувати все

class abituraForm(forms.ModelForm):

    class Meta:
        model = abitura
        exclude = [""]

