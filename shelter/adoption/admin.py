from django.contrib import admin

# Register your models here.

from .models import Dog, Breed

admin.site.register(Dog)
admin.site.register(Breed)
