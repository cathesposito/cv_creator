from django.forms import ModelForm
from .models import PersonalInfo


class PersonalInfoInputForm(ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'