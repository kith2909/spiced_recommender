from django import forms
from django.forms import inlineformset_factory
from .models import Profile, Answer

QuestionFormSet = inlineformset_factory(
    Profile,
    Answer,
    fields=('hobbies',
            'mean_age',
            'work_in_team',
            'stubbornness_rate',
            'location',
            'subjects',
            'feedback',
            'lang',
            'responsible',
            'logic_1',
            'logic_2',
            'tech_1',
            'tech_2'),
    extra=0,
    widgets={
        'hobbies': forms.Textarea(attrs={'class': 'form-control'}),
        'mean_age': forms.NumberInput(attrs={'class': 'form-control'}),
        'work_in_team': forms.CheckboxInput(attrs={'class': 'custom-checkbox'}),
        'stubbornness_rate': forms.NumberInput(attrs={'class': 'select-control'}),
        'location': forms.TextInput(attrs={'class': 'form-control'}),
        'subjects': forms.TextInput(attrs={'class': 'form-control'}),
        'feedback': forms.Textarea(attrs={'class': 'form-control'}),
        'lang': forms.Select(choices=[(1, 'A1'), (2, 'A2'), (3, 'B1'), (4, 'B2'), (5, 'C1'), (6, 'Native')],
                             attrs={'class': 'form-control'}),
        'responsible': forms.Select(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
                                    attrs={'class': 'form-control'}),
        'logic_1': forms.Select(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
                                attrs={'class': 'form-control'}),
        'logic_2': forms.Select(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
                                attrs={'class': 'form-control'}),
        'tech_1': forms.Select(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
                               attrs={'class': 'form-control'}),
        'tech_2': forms.Select(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
                               attrs={'class': 'form-control'}),
    }
)
