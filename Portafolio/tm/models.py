from django.db import models

# Create your models here.
class addticket(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    severidad=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    tecnologia=models.CharField(max_length=30)
    owner=models.CharField(max_length=30)
    document=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-created"]

    def __str__(self):
        return self.title