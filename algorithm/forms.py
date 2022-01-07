from django import forms


ALGORITHM_CHOICES = [
    ('bubblesort', 'Bubble Sort'),
    ('insertionsort', 'Insertion Sort'),
]

class sortingForm(forms.Form):
    numbers = forms.CharField(label='numbers', max_length=100)
    algorithm = forms.CharField(label='Select your algorithm', widget=forms.Select(choices=ALGORITHM_CHOICES))
    