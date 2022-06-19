from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

GENDER_C = (
    ('선택안함', '선택안함'), ('여성', '여성'),
    ('남성', '남성'), )

class User(AbstractUser):
    gender = models.CharField(max_length=10, choices=GENDER_C, default='N')
    birthdate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=15)
    city = models.CharField(max_length=30)



class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d%H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

