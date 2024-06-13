from django.db import models
class Cheatsheet(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='downloadfile/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Загрузить файл"
        verbose_name_plural = "Загрузить файлы"  
        
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"  
        verbose_name_plural = "Новости" 