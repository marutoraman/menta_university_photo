from django.forms import ModelForm, ChoiceField, CharField, Textarea
from myapp.models import EditUser

class EditUserForm(ModelForm):
    class Meta:
        model = EditUser
        fields = ("nickname",)
