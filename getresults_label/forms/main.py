from django import forms

from edc.base.form.forms import BaseModelForm

from ..models import ZplTemplate, LabelPrinter


class LabelForm(BaseModelForm):

    identifier = forms.CharField(
        max_length=25,
        label="Identifier",
        help_text="",
        error_messages={'required': 'Please enter a valid identifier.'})


class ZplTemplateForm (BaseModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    class Meta:
        model = ZplTemplate


class LabelPrinterForm (BaseModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    class Meta:
        model = LabelPrinter
