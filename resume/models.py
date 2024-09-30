from django.db import models


class Biodata(models.Model):
    pdf = models.FileField(upload_to='resume/')
    
    def __str__(self):
        return str(self.id)

class Profession_Video(models.Model):
    url= models.TextField() 
    
    def __str__(self):
        return str(self.id)        
