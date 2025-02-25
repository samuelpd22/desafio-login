from django.urls import path

from mypage.views import login_view, registro

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
]
