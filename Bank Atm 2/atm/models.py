from django.db import models


class ATM(models.Model):
    id = models.AutoField(primary_key=True)
    atm_location = models.CharField(max_length=200)
    max_withdrawal = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.atm_location
