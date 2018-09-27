from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(blank=True, verbose_name="Project Image")
    link=models.URLField(null=True, verbose_name="Project URL")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-created"]

    def __str__(self):
        return self.title