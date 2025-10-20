from django.contrib import admin
from .models import contact,homecontact,admin_home,admin_home2,admin_about,Music

# Register your models here.
class adminhomecontact(admin.ModelAdmin):
    list_display=('name','mail')

class admincontact(admin.ModelAdmin):
    list_display=('name','email','subject','message')

class adminhome(admin.ModelAdmin):
    list_display=('image',)

class adminhome2(admin.ModelAdmin):
    list_display=('img','link')

class adminabout(admin.ModelAdmin):
    list_display=('image',)

admin.site.register(homecontact,adminhomecontact)
admin.site.register(contact,admincontact)
admin.site.register(admin_home,adminhome)
admin.site.register(admin_home2,adminhome2)
admin.site.register(admin_about,adminabout)



# new code

admin.site.register(Music)