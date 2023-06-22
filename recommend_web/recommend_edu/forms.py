from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    hobbies = forms.CharField(label='Enter your hobbies here',
                              widget=forms.Textarea(attrs={'class': 'form-control'}))
    mean_age = forms.IntegerField(label='Please write you age',
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    work_in_team = forms.BooleanField(label='Will you prefer work in team most of the time, than alone?',
                                      help_text='Check, if you prefer to work with people',
                                      required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'}))
    stubbornness_rate = forms.IntegerField(label='People always more important, than goals. Rate 0, if you totally disagree'
                                                 'and rate 5 if you totally agree with this frase',
                                           widget=forms.NumberInput(attrs={'class': 'select-control'}))
    location = forms.CharField(label='Location', help_text='Enter your location',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    subjects = forms.CharField(label='Write two favorite subjects in school or university',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    feedback = forms.CharField(
        label="For what skills you've got the best feedback from your colleagues or friends in last 3 years",
        help_text='Enter best feedback in few words',
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    lang = forms.ChoiceField(
        label='What is your level for national language in country, that you want to  study or work?',
        choices=[(1, 'A1'), (2, 'A2'), (3, 'B1'), (4, 'B2'), (5, 'C1'), (6, 'Native')],
        widget=forms.Select(attrs={'class': 'form-control'}))
    responsible = forms.ChoiceField(label='If there is a less pleasant task, that I need to do: \n'
                                          '1. I will still finish it because it iss my responsibility\n'
                                          '2. Instead of stressing me out, I would better find someone else to do it,'
                                          ' and then I just check.\n'
                                          '3. I have the right to protest to my boss\n'
                                          '4. I will try finish it even though it feels heavy, but do it as slow as possible\n'
                                          '5. I ask my co-workers to help solve it, but do it mostly myself',
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
