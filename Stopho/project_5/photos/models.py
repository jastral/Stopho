from django.db import models
import datetime
from django.urls import reverse

# Create your models here.
class UploadImages(models.Model):
    slug = models.SlugField(max_length=200, db_index=True, default='')
    image = models.ImageField(upload_to="user_images/%Y/%m/%D/")
    description = models.CharField(max_length=100)
    added_on = models.DateField(default=datetime.date.today)

    class Meta: 
        verbose_name = 'image'
        verbose_name_plural = 'photos'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('photos:image_list', args=[self.slug])
