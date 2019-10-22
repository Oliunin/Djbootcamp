from django.urls import path
from AppTwo import views
from AppTwo.views import gethouses, getcompanies



urlpatterns = [
    path('', views.NewUser),
    path('help', views.help),
    path('users/',views.users),
    # path('map/',views.Complist),
    path('gethouses/', gethouses.as_view()),
    path('getcompanies/',getcompanies.as_view()),
]
