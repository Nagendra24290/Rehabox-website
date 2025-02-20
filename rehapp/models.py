from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    condition = models.CharField(max_length=200)
    last_visit = models.DateField()
    
    
    def __str__(self):
        return self.name




