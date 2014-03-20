from django.contrib import admin
from mailarchive.models import Address, Account, HeaderInfo,  Mail

admin.site.register(Address)
admin.site.register(Account)
admin.site.register(HeaderInfo)
admin.site.register(Mail)
