from django import forms

class FileFormatSelectForm(forms.Form):
    file_formats = forms.MultipleChoiceField(
        required=True,
        label='Please choose file format of the generated output',
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('csv', 'csv'), ('excel', 'excel'), ('json', 'json')
        ],
    )
