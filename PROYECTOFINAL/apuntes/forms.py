from django.forms import ModelForm
from .models import Apunte

class ApunteForm(ModelForm):
    class Meta:
        model = Apunte
        fields = ['titulo', 'contenido', 'portada', 'creador']
        exclude = ["creador"]