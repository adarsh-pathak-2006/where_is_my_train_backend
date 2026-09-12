from django.db import models

class Station(models.Model):
    name=models.CharField(max_length=300)
    state=models.CharField(max_length=100)
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
