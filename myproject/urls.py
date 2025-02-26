from django.urls import path
from django.views.generic.base import RedirectView

from mypage.views import login_view, registro

urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False)),  
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
]
