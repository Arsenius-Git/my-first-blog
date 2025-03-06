from django import forms
from .models import ExpensesTrack

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    check = forms.BooleanField(required=False)

class GetUrl(forms.Form):
    url = forms.CharField(label = "url", max_length=200)

class Transaction(forms.ModelForm):
    class Meta:
        model = ExpensesTrack
        fields = ["description", "amount"]
        widgets = {
            "description": forms.TextInput(attrs={'placeholder': 'Enter description'}),
            "amount": forms.NumberInput(attrs={'placeholder': 'Enter amount (use - for expenses)'})
        }
