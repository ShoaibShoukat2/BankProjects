from django.db import models
from customer.models import Customer


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
