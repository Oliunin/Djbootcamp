from django import forms
from AppTwo.models import My_user

class NewUserForm(forms.ModelForm):
    class Meta:
        model = My_user
        fields = '__all__'
