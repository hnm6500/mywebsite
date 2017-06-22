from django.contrib import admin

# Register your models here.
from.models import PersonalInformation,Myobjective,myprojects,Messages
# Register your models here.
admin.site.register(PersonalInformation)
admin.site.register(Myobjective)
admin.site.register(myprojects)
admin.site.register(Messages)