from django import forms
from .models import Transaction,Category


class TransactionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )    
    class Meta:
        model = Transaction
        fields = [ 'amount', 'type', 'category', 'date']