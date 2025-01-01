
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.hello)
    # path('',views.converts,name='coverts'),
    path('hello',views.hello,name='hello'),
    path('converting/',views.converting,name="converting"),
    path('',views.login,name='login'),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name='logout')

    
    
]