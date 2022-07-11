from django.contrib import admin
from .models import Todo

# Класс для кастомизации админки, в данном случае делает поле "created" видимым
class Todoadmin(admin.ModelAdmin):
    readonly_fields = ('created'),

admin.site.register(Todo, Todoadmin)

