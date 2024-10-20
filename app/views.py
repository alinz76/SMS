from django.shortcuts import render
from urllib.parse import urlencode
from base64 import b64encode
from .forms import SMSForm
import requests


# Create your views here.
def home_page(request):
    sms_form = SMSForm()
    context = {'sms_form': sms_form}
    if request.method == 'POST':
        url = 'https://smspanel.trez.ir/SendPatternWithUrl.ashx?'
        username = request.POST.get('username')
        password = request.POST.get('password')
        idendity = f'{username}:{password}'
        # userAndPass = urlencode(idendity)
        bytestr = bytes(idendity, encoding="ascii")
        userAndPass = b64encode(bytestr).decode("ascii")
        headers = { 'Authorization' : 'Basic %s' %  userAndPass , 'Content-type': 'application/json' , 'encoding':'utf-8'}
        link = f'{url}AccessHash={request.POST.get('access_hash')}&PhoneNumber={request.POST.get('phone_number')}&PatternId={request.POST.get("pattern_id")}&RecNumber={request.POST.get("rec_number")}&SmsClass={request.POST.get("sms_class")}'
        print(link)
        data = requests.get(link, headers=headers)
        response = data.text
        print(response)
        return render(request, 'app/homepage.html', context=context)
    return render(request, 'app/homepage.html', context=context)
