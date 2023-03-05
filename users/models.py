
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models 
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s profile"
    
    def save_pic(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 and img.width > 300:
           new_size=(300,300)
           img.thumbnail(new_size)
           img.save(self.image.path)
           


