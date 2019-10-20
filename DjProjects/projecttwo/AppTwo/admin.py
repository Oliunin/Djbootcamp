from django.contrib import admin
from AppTwo.models import My_user
from AppTwo.models import Company
from AppTwo.models import House
# Register your models here.

admin.site.register(My_user)
admin.site.register(Company)
admin.site.register(House)
