from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    hobbies = forms.CharField(label='Hobbies', help_text='Enter your hobbies here',
                              widget=forms.Textarea(attrs={'class': 'form-control'}))
    mean_age = forms.IntegerField(label='Mean Age', help_text='Enter the mean age',
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    work_in_team = forms.BooleanField(label='Work in Team', help_text='Check if you work well in a team',
                                      required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'}))
    stubbornness_rate = forms.IntegerField(label='Stubbornness Rate', help_text='Enter the stubbornness rate',
                                           widget=forms.NumberInput(attrs={'class': 'select-control'}))
    location = forms.CharField(label='Location', help_text='Enter your location',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    subjects = forms.CharField(label='Subjects', help_text='Enter your subjects',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    feedback = forms.CharField(label='Feedback', help_text='Enter your feedback',
                               widget=forms.Textarea(attrs={'class': 'form-control'}))
    lang = forms.ChoiceField(label='Language Level',
                             choices=[(1, 'A1'), (2, 'A2'), (3, 'B1'), (4, 'B2'), (5, 'C1'), (6, 'Native')],
                             widget=forms.Select(attrs={'class': 'form-control'}))
    responsible = forms.ChoiceField(label='Responsibility Level',
                                    choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    logic_1 = forms.ChoiceField(label='Logic 1', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
                                widget=forms.Select(attrs={'class': 'form-control'}))
    logic_2 = forms.ChoiceField(label='Logic 2', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
                                widget=forms.Select(attrs={'class': 'form-control'}))
    tech_1 = forms.ChoiceField(label='Tech 1', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
                               widget=forms.Select(attrs={'class': 'form-control'}))
    tech_2 = forms.ChoiceField(label='Tech 2', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
                               widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Answer
        fields = '__all__'

    class Meta:
        model = Answer
        fields = '__all__'
