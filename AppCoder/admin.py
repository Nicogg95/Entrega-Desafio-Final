from django.contrib import admin

from AppCoder.views import *

from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Juego)
admin.site.register(Avatar)
