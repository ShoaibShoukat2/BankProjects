from django.db import models
from django.urls import reverse

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cpr = models.CharField(max_length=20)
    account_no = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=4)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer:customer_detail', args=[str(self.pk)])
