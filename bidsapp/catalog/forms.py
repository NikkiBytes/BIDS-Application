from django import forms

class OsirixForm(forms.Form)
    subject = forms.Charfield()
    directory = forms.Charfield()


    def get_data(self):

        pass
