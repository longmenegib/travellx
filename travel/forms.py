from django import forms
from .models import Registration_form, Ticket
from django.contrib.auth.models import User


OPTIONS = (
        ('bamenda', 'Bamenda'),
        ('douala', 'Douala'),
        ('yaounde', 'Yaounde'),
        ('buea', 'Buea'),
        ('bafoussam', 'Bafoussam'),
        ('ngaoundere', 'Ngaoundere'),
        )
moment = (
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        )


class Reg(forms.ModelForm):
    class Meta:
        model = Registration_form
        fields = '__all__'

class TicketForm(forms.ModelForm):


    source = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)
    destination = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)
    time = forms.ChoiceField(widget=forms.Select, choices=moment)
#     date = forms.DateTimeField()
    id_number = forms.CharField(max_length=50)
    class Meta:
        model = Ticket
        fields = ('source','destination', 'date','time', 'id_number', 'user')

class Signing(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')