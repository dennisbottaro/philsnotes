from django import forms
from django.forms import ModelForm
from .models import Job, JobNote, Builder
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'
    initial = datetime.date.today


class JobNoteForm(ModelForm):
    class Meta:
        model = JobNote
        fields = ['note_date', 'note_text']
        widgets = {
            'note_text': forms.Textarea(attrs={'rows': '3'}),
        }


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class BuilderForm(ModelForm):
    class Meta:
        model = Builder
        fields = '__all__'
