from django import forms
from .models import Resena

class ResenaForm(forms.ModelForm):
    CALIFICACION_CHOICES=[]
    CALIFICACION_CHOICES.append((1, '1 ( basico )'))
    CALIFICACION_CHOICES.append((2, '2 ( normal )'))
    CALIFICACION_CHOICES.append((3, '3 ( bueno )'))
    CALIFICACION_CHOICES.append((4, '4 ( muy bueno )'))
    CALIFICACION_CHOICES.append((5, '5 ( exelente )'))
    calificacion=forms.ChoiceField(choices=CALIFICACION_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model=Resena
        fields=['nombre', 'comentario', 'calificacion']
        labels={'nombre':'Nombre:', 'comentario': 'Comentario:', 'calificacion':'Calificacion'}