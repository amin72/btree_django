from django.urls import path
from . import views


app_name = 'pages'

urlpatterns = [
    # index
    path('', views.index, name='index'),
    
    # about
    path('about/', views.about, name='about'),
]
