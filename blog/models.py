from django.db import models




class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False, max_length=300)
    url = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/images/')

    def __str__(self) -> str:    #выводим название заголовков в админку
        return self.title