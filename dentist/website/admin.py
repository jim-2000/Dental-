from django.contrib import admin
from .models import get_in_touch, appoinment,news

# Register your models here.

admin.site.register(get_in_touch)
admin.site.register(appoinment)
admin.site.register(news)
