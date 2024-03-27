from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name









# Create your models here.
