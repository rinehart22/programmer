from django.db import models

# Create your models here.
class programmer(models.Model):
    Name = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    skill = models.CharField(max_length=30)
    tools = models.CharField(default= '0',max_length=80)
     
   
    image = models.ImageField(blank= True, null= True, upload_to= "images/")
    def __str__(self):
        return self.Name