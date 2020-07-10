from django.db import models

# Create your models here.
class get_in_touch(models.Model):
    massage_name = models.CharField(max_length = 20)
    massage_Email  = models.EmailField(max_length = 50)
    user_phone = models.CharField(max_length = 15)
    user_subjects = models.CharField(max_length = 30)
    massage = models.TextField()
    
    def __str__(self):
        return self.massage_name
    

class appoinment(models.Model):
    ur_name = models.CharField(max_length = 20)
    ur_phone = models.CharField(max_length = 15)
    ur_email = models.EmailField(max_length = 20)
    ur_Address = models.TextField(max_length = 200)
    ur_time = models.CharField(max_length = 20)
    ur_date = models.CharField(max_length = 20)
    ur_mass = models.TextField(max_length = 299)

    def __str__(self):
        return self.ur_name
    
class news(models.Model):
    email = models.EmailField(max_length = 20)

    def __str__(self):
        return self.email
    