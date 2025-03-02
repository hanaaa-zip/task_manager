from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']  # ✅ Add 'status'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),  # ✅ Date Picker
            'status': forms.Select(choices=Task.STATUS_CHOICES),  # ✅ Dropdown for status
        }
