from django.contrib import admin
from .models import Profiles

class AccountsAdmin(admin.ModelAdmin):
    class Meta:
        model = Profiles

admin.site.register(Profiles, AccountsAdmin)
