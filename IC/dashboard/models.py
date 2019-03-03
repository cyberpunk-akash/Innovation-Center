from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User=get_user_model()
import misaka

class Post(models.Model):
    startup_name=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    # related name used in views.py in startup_post=prefetch data
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now=True)
    admin_name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    description=models.TextField()
    # description_html=models.TextField(editable=False)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.description_html=misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('dashboard:single',kwargs={'username':self.startup_name.username,'pk':self.pk})



    class Meta:
        ordering=["-created_at"]
