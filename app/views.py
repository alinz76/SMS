from django.shortcuts import render
from django.contrib import messages
from base64 import b64encode
from . import forms
import requests
import datetime


def home_page(request):
    return render(request, 'app/homepage.html')    



def SendPatternWithUrl(request):
    sms_form = forms.SendPatternWithUrl()
    context = {'sms_form': sms_form}
    if request.method == 'POST':
        url = 'https://smspanel.trez.ir/SendPatternWithUrl.ashx?'
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # idendity = f'{username}:{password}'
        # bytestr = bytes(idendity, encoding="ascii")
        # userAndPass = b64encode(bytestr).decode("ascii")
        # headers = { 'Authorization' : 'Basic %s' %  userAndPass , 'Content-type': 'application/json' , 'encoding':'utf-8'}
        link = f'{url}AccessHash={request.POST.get('access_hash').strip()}&PhoneNumber={request.POST.get('phone_number')}&PatternId={request.POST.get("pattern_id").strip()}&RecNumber={request.POST.get("rec_number")}&SmsClass={request.POST.get("sms_class")}&token1={request.POST.get("token1")}&token2={request.POST.get('token2')}&token3={request.POST.get('token3')}&token4={request.POST.get('token4')}&token5={request.POST.get('token5')}&token6={request.POST.get('token6')}&token7={request.POST.get('token7')}&token8={request.POST.get('token8')}&token9={request.POST.get('token9')}'
        print(link)
        data = requests.get(link)
        response = data.text
        print(response)
        if int(response) > 2000:
            messages.success(request, 'با موفقیت ارسال شد')
        else:
            messages.warning(request, f"خطای {response} رخ داد")
    
    return render(request, 'app/SendPatternWithUrl.html', context=context)
def SendPatternCodeWithUrl(request):
    sms_form = forms.SendPatternCodeWithUrl()
    context = {'sms_form': sms_form}
    if request.method == 'POST':
        url = 'https://smspanel.trez.ir/SendPatternCodeWithUrl.ashx'
        Access_Hash = request.POST.get('access_hash')
        Mobile = request.POST.get('mobile')
        Pattern_Id = request.POST.get('pattern_id')
        token1 = request.POST.get('token1')
        token2 = request.POST.get('token2')
        token3 = request.POST.get('token3')
        token4 = request.POST.get('token4')
        token5 = request.POST.get('token5')
        token6 = request.POST.get('token6')
        token7 = request.POST.get('token7')
        token8 = request.POST.get('token8')
        token9 = request.POST.get('token9')
        multipart_data = {
            'AccessHash': (None, Access_Hash),
            'Mobile': (None, Mobile),
            'PatternId': (None, Pattern_Id),
            'token1': (None, token1),
            'token2': (None, token2),
            'token3': (None, token3),
            'token4': (None, token4),
            'token5': (None, token5),
            'token6': (None, token6),
            'token7': (None, token7),
            'token8': (None, token8),
            'token9': (None, token9),
        }
        print(multipart_data) 
        response = requests.post(url=url, files=multipart_data)
        response_text = response.text
        print(response_text)
        if int(response_text) > 2000:
                messages.success(request, 'با موفقیت ارسال شد')
        else:
            messages.warning(request, f"خطای {response_text} رخ داد")
    return render(request, 'app/SendPatternCodeWithUrl.html', context=context)


def SendPatternWithPost(request):
    sms_form = forms.SendPatternWithPost()
    context = {'sms_form': sms_form}
    if request.method == 'POST':
        url = 'https://smspanel.trez.ir/SendPatternWithPost.ashx'
        access_hash = request.POST.get('access_hash')
        phone_number = request.POST.get('phone_number')
        pattern_id = request.POST.get('pattern_id')
        token1 = request.POST.get('token1')
        token2 = request.POST.get('token2')
        token3 = request.POST.get('token3')
        token4 = request.POST.get('token4')
        token5 = request.POST.get('token5')
        token6 = request.POST.get('token6')
        token7 = request.POST.get('token7')
        token8 = request.POST.get('token8')
        token9 = request.POST.get('token9')
        RecNumber = request.POST.get('rec_number')
        smsclass = request.POST.get('sms_class')
        multipart_data = {
            'AccessHash': (None, access_hash),
            'PhoneNumber': (None, phone_number),
            'PatternId': (None, pattern_id),
            'token1': (None, token1),
            'token2': (None, token2),
            'token3': (None, token3),
            'token4': (None, token4),
            'token5': (None, token5),
            'token6': (None, token6),
            'token7': (None, token7),
            'token8': (None, token8),
            'token9': (None, token9),
            'RecNumber': (None, RecNumber),
            'Smsclass': (None, smsclass),
        }
        
        print(multipart_data) 
        response = requests.post(url=url, files=multipart_data)
        response_text = response.text
        print(response_text)
        if int(response_text) > 2000:
                messages.success(request, 'با موفقیت ارسال شد')
        else:
            messages.warning(request, f"خطای {response_text} رخ داد")

    return render(request, 'app/SendPatternWithPost.html', context=context)


def SendGroupSms(request):
    url = 'https://smspanel.trez.ir/api/smsApiWithPattern/SendMessage/'
    sms_form = forms.SendGroupSms()
    context = {
         'sms_form': sms_form
    }
    if request.method == 'POST':
        username = 'alinz76'
        password = 'testing123'
        idendity = f'{username}:{password}'
        bytestr = bytes(idendity, encoding="ascii")
        userAndPass = b64encode(bytestr).decode("ascii")
        headers = { 'Authorization' : 'Basic %s' %  userAndPass , 'Content-type': 'application/x-www-form-urlencoded' , 'encoding':'utf-8'}
        access_hash = request.POST.get('access_hash')
        phone_number = request.POST.get('phone_number')
        pattern_id = request.POST.get('pattern_id')
        token1 = request.POST.get('token1')
        token2 = request.POST.get('token2')
        token3 = request.POST.get('token3')
        token4 = request.POST.get('token4')
        token5 = request.POST.get('token5')
        token6 = request.POST.get('token6')
        token7 = request.POST.get('token7')
        token8 = request.POST.get('token8')
        token9 = request.POST.get('token9')
        mobiles = request.POST.get('mobiles').split('\r\n')
        user_group_id = request.POST.get('user_group_id')
        senddateintimestamp = request.POST.get('senddateintimestamp')
        date_time_obj = datetime.datetime.strptime(senddateintimestamp, '%Y-%m-%dT%H:%M')
        # Convert the datetime object to a Unix timestamp
        unix_timestamp = int(date_time_obj.timestamp())
        multipart_data = {
            'AccessHash': access_hash,
            'PhoneNumber': phone_number,
            'PatternId': pattern_id,
            'token1': token1,
            'token2': token2,
            'token3': token3,
            'token4': token4,
            'token5': token5,
            'token6': token6,
            'token7': token7,
            'token8': token8,
            'token9': token9,
            'Mobiles' : mobiles,
            'UserGroupID' : user_group_id,
            'SendDateInTimeStamp' : unix_timestamp
        }

        print(multipart_data)
        response = requests.post(url, headers=headers, data=multipart_data)
        if response:
            response_text = response.text
            print(response_text)
            if int(response_text) > 2000:
                    messages.success(request, 'با موفقیت ارسال شد')
            else:
                messages.warning(request, f"خطای {response_text} رخ داد")

    return render(request, 'app/sendgroupsms.html', context=context)
