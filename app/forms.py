from django import forms


class SMSForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    access_hash = forms.CharField(max_length=100)
    phone_number = forms.IntegerField()
    pattern_id = forms.CharField(max_length=100)
    rec_number = forms.CharField(max_length=100)
    sms_class = forms.IntegerField()
    token1 = forms.CharField(max_length=100, required=False)
    token2 = forms.CharField(max_length=100, required=False)
    token3 = forms.CharField(max_length=100, required=False)
    token4 = forms.CharField(max_length=100, required=False)
    token5 = forms.CharField(max_length=100, required=False)
    token6 = forms.CharField(max_length=100, required=False)
    token7 = forms.CharField(max_length=100, required=False)
    token8 = forms.CharField(max_length=100, required=False)
    token9 = forms.CharField(max_length=100, required=False)
