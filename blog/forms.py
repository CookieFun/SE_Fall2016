from django import forms


class UploadFileForms(forms.Form):
    upload_file = forms.FileField(
        label='upload a file'
    )
