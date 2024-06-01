from django import forms
import datetime

class PlayFrom(forms.Form):
    name = forms.CharField(min_length=10, label="Full Name", initial="Mr ")
    comment = forms.ChoiceField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    email = forms.EmailField(help_text="Enter your email")
    
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    
    # DateField with SelectedDateWidget
    BIRTH_YEAR_CHOICE = ['1997','1998','1999']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICE))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    
    favorite_color_select = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    
    COURSES_CHOICE = [
        ('bangla', 'Bangla'),
        ('english', 'English'),
        ('math', 'Math'),
    ]
    
    courses = forms.MultipleChoiceField(choices=COURSES_CHOICE)
    
    multiple_courses_checkbox = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=COURSES_CHOICE)
    
    agree = forms.BooleanField(initial=True)