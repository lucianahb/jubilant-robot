from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'Name: {self.name} | Email: {self.email}'
