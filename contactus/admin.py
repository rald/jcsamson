from django.contrib import admin

from .models import ContactData


class ContactDataInline(admin.TabularInline):
  model=ContactData
  extra=1

class ContactDataAdmin(admin.ModelAdmin):
  fields = ('full_name','email','date_entry','photo')
  list_display = ('full_name','email','date_entry','photo')
  inlines=[ContactDataInline]

admin.site.register(ContactData)
