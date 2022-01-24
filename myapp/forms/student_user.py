from django.forms import ModelForm, ChoiceField, CharField, Textarea
from myapp.models import StudentUser

class StudentUserForm(ModelForm):
    
    class Meta:
        model = StudentUser
        fields = ("nickname", "university_name", "major_name")