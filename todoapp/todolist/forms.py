from django import forms
from django.core.exceptions import RequestDataTooBig
from django.forms import ModelForm
from .models import Task
from django.contrib.auth import get_user_model


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__" 


    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter task...",
            }
        ),
    )

    completed = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(attrs={"class": "form-check-input"}),
    )

