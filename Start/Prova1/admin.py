from django.contrib import admin
from Prova1.models import AccessRecord,Topic,Webpage,AppUser
from Prova1.models import UserProfileInfo, User
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AppUser)
admin.site.register(UserProfileInfo)