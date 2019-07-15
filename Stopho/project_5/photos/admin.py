from django.contrib import admin
from .models import UploadImages

# Register your models here.
class UploadImagesAdmin(admin.ModelAdmin):
    list_display = ['image']
    prepopulated_fields = {'slug':('image',)}
admin.site.register(UploadImages, UploadImagesAdmin)
