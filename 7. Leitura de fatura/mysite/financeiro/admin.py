from django.contrib import admin

from .models import BankAccount,Entry,Exit

admin.site.register(Entry)
admin.site.register(Exit)
