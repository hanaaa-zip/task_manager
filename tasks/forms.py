from django import forms
from .models import Task  # ✅ Correctly importing the Task model

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']  
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),  # ✅ Date Picker
            'description': forms.Textarea(attrs={'rows': 3}),  # ✅ textarea
        }
