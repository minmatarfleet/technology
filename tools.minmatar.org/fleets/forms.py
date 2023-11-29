from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse
from .models import EveDoctrine, EveFleet, fleet_types
from contracts_v2.models import EveContractLocation
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.utils import timezone
from .time import get_time_choices

def get_time():
    return timezone.now()

class EveFleetForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=DateTimePickerInput(), required=True, initial=get_time)
    end_time = forms.DateTimeField(widget=DateTimePickerInput(), required=False)
    doctrine = forms.ModelChoiceField(EveDoctrine.objects, empty_label="Other", required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
   

    class Meta:
        model = EveFleet
        fields = ['type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('create_fleet')
        self.helper.add_input(Submit('submit', 'Submit'))

class EveFleetEditForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=DateTimePickerInput(), required=True, initial=get_time)
    end_time = forms.DateTimeField(widget=DateTimePickerInput(), required=False)
    staging = forms.ModelChoiceField(EveContractLocation.objects, empty_label="Other", required=True)
    doctrine = forms.ModelChoiceField(EveDoctrine.objects, empty_label="Other", required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = EveFleet
        fields = [
            'type'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))