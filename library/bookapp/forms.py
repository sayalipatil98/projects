from django import forms
from .models import book

class bookform(forms.ModelForm):
    class Meta:
        model=book
        fields="__all__"
        labels={
            "bookid":"BOOK ID",
            "booknm":"BOOK NAME",
            "bookpublisher":"BOOOK PUBLISHER",
            "bookpr":"BOOK PRICE"
        }
        widgets={
            "bookid":forms.NumberInput(attrs={
                "class":"class-control",
                "palceholder":"eg.10101"
            }),
            "booknm": forms.TextInput(attrs={
                "class": "class-control",
                "palceholder": "eg.PYTHON"
            }),
            "bookpublisher": forms.TextInput(attrs={
                "class": "class-control",
                "palceholder": "eg.A.N.Patil"
            }),
            "bookpr": forms.NumberInput(attrs={
                "class": "class-control",
                "palceholder": "eg.3000"
            })
        }