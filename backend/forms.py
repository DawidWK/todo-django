from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    task = form.CharField(widget=forms.TextInput(
        attrs = {
            'class':'form-control',
        }
    ))

    class Meta:
        model = Task
        fields = ('task',)