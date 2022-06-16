from django import forms
from .models import UserReservation


class UserReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text",
                               'name': "name",
                               'class': "form-input form-control-has-validation",
                               'id': "name",
                               'placeholder': "Your Name",
                               'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars"
                           }))
    phone = forms.CharField(max_length=15,
                            widget=forms.TextInput(
                                attrs={'type': 'text', 'name': 'phone', 'id': 'phone', 'class': 'form-input form-control-has-validation',
                                       'placeholder': 'Телефон', 'required': 'required',
                                       'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))
    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': "number",
        'class': "form-input form-control-has-validation",
        'name': "people",
        'id': "people",
        'placeholder': "# of people",
        'data-rule': "minlen:1",
        'data-msg': "Please enter at least 1 chars"}))

    message = forms.CharField(max_length=400,
                              widget=forms.Textarea(
                                  attrs={'type': 'message', 'name': 'message', 'class': 'form-input form-control-has-validation',
                                         'rows': '5', 'placeholder': 'Сообщение', 'required': 'required'}))

    class Meta:
        model = UserReservation
        fields = ('name', 'phone', 'persons', 'message')