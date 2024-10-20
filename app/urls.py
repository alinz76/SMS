from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    # path('send_sms/', views.SendPatternWithUrlView.as_view(), name='send-sms'),
]