
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.hello)
    # path('',views.converts,name='coverts'),
    path('',views.hello),
    path('converting/',views.converting,name="converting"),

    
    
]