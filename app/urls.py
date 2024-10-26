from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('sendpatternwithurl/', views.SendPatternWithUrl, name='send-pattern'),
    path('sendpatterncodewithurl/', views.SendPatternCodeWithUrl, name='send-pattern-code'),
    path('sendpatternwithpost/', views.SendPatternWithPost, name='send-pattern-post'),
    path('sendgroupsms/', views.SendGroupSms, name='send-group-sms'),
]