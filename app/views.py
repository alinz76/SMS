from django.shortcuts import render
from django.contrib import messages
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
        bytestr = bytes(idendity, encoding="ascii")
        userAndPass = b64encode(bytestr).decode("ascii")
        headers = { 'Authorization' : 'Basic %s' %  userAndPass , 'Content-type': 'application/json' , 'encoding':'utf-8'}
        link = f'{url}AccessHash={request.POST.get('access_hash').strip()}&PhoneNumber={request.POST.get('phone_number')}&PatternId={request.POST.get("pattern_id").strip()}&RecNumber={request.POST.get("rec_number")}&SmsClass={request.POST.get("sms_class")}&token1={request.POST.get("token1")}'
        print(link)
        data = requests.get(link, headers=headers)
        response = data.text
        print(response)
        if response:
            if int(response) > 2000:
                messages.success(request, 'با موفقیت ارسال شد')
        else:
            messages.error(request, "خطایی رخ داد")
        return render(request, 'app/homepage.html', context=context)
    return render(request, 'app/homepage.html', context=context)
