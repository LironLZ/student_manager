from django import forms
from .models import Student, Assignment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_class', 'phone']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'status']

    due_date = forms.DateField(widget=forms.SelectDateWidget())