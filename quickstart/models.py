from django.db import models
 
class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    name = models.TextField()
 
    def __str__(self) -> str:
        return self.title