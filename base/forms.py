from django.forms import ModelForm
from .models import Room
from django.forms import ModelForm , TextInput ,Textarea

class RoomForm(ModelForm):  
    class Meta:
        model = Room  
        fields =  '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'enter the room name'
                }),
            'description':Textarea(attrs={
                'class':'form-control',
                'style':'max-width:300px',
                'placeholder':"write descriptions here ...."
            })    
        }