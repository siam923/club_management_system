from django import forms
from django.contrib.admin import widgets
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['mydate'].widget = widgets.AdminDateWidget()
        self.fields['mytime'].widget = widgets.AdminTimeWidget()
        self.fields['mydatetime'].widget = widgets.AdminSplitDateTime()
