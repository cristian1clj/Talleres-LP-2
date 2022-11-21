from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=40)
    password = models.CharField(max_length=80)
    
    def __str__(self) -> str:
        return self.username