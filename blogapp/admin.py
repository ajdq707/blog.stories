from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import postdb, postab, sidepost, aboutme

admin.site.register(postdb)
admin.site.register(postab)
admin.site.register(sidepost)
admin.site.register(aboutme)