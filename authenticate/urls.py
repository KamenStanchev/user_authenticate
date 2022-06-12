
from django.contrib import admin
from django.urls import path
from authenticate.views import home


from authenticate.views import home, signup, signin, signout

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup_page'),
    path('signin/', signin, name='signin_page'),
    path('signout/', signout, name='signout_page'),
]
