from django.urls import path
from AppTwo import views

urlpatterns = [
    path('', views.NewUser),
    path('help', views.help),
    path('users/',views.users),
    path('map/',views.Houselist),
]
