from django.forms import ModelForm
from .models import Task, Tag

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'