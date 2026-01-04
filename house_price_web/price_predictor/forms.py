from django import forms

class HousePriceForm(forms.Form):
    area = forms.FloatField(
        min_value=300,
        max_value=10000,
        label="Area (sq ft)",
        help_text="Typical range: 500 - 4000 sq ft",
        widget=forms.NumberInput(attrs={
            'step': '50'
        })
    )

    bedrooms = forms.IntegerField(
        min_value=1,
        max_value=10,
        label="Bedrooms",
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 3'
        })
    )

    bathrooms = forms.IntegerField(
        min_value=1,
        max_value=10,
        label="Bathrooms",
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 2'
        })
    )

    age = forms.IntegerField(
        min_value=0,
        max_value=100,
        label="Age of House (years)",
        widget=forms.NumberInput(attrs={
            'type': 'range',
            'step': '1'
        })
    )