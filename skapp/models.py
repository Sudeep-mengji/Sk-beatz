from django.db import models

# Create your models here.
class homecontact(models.Model):
    name=models.CharField(max_length=200, null=True)
    mail=models.CharField(max_length=200, null=True)

class contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=200, null=True)

# admin models

class admin_home(models.Model):
    image=models.FileField(upload_to="photo/", max_length=500,null=True,default=None)

class admin_home2(models.Model):
    img=models.FileField(upload_to="photo/",max_length=500,null=True,default=None)
    link=models.CharField(max_length=200,null=True,default=None)

class admin_about(models.Model):
    image=models.FileField(upload_to="photo/", max_length=500,null=True,default=None)


# new code
class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')
    album_art = models.ImageField(upload_to='album_art/', null=True, blank=True)

    def __str__(self):
        return self.title