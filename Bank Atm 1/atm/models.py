from django.db import models

class ATM(models.Model):
    id = models.AutoField(primary_key=True)
    atm_location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.atm_location
