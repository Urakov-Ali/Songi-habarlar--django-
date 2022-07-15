from django.db import models
from django.urls import reverse

class Categorie(models.Model):
    Name =models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Post(models.Model):
    Title =models.CharField(max_length=100, null=False, blank=True)
    Image =models.ImageField(upload_to='media/', blank=True)
    Text =models.TextField()
    Category =models.ForeignKey(Categorie, blank=False, null=True, on_delete=models.SET_NULL)
    Creation_date =models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('page_view', kwargs={'page_id':self.pk})

    def __str__(self):
        return self.Title


