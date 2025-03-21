from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):

  CATEGORY = [
    ('Tech', 'Tech'),
    ('News', 'News'),
    ('Gadget', 'Gadget'),
    ('Programming', 'Programming')
  ]
  
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  image = models.ImageField(upload_to ="Featured/")
  alt = models.CharField(max_length = 100)
  title = models.CharField(max_length = 200)
  text = RichTextUploadingField()
  meta_description = models.TextField(max_length=150)
  published_date = models.DateTimeField(auto_now_add = True)
  category = models.CharField(max_length=20, choices=CATEGORY, default="Tech")

  def __str__(self):
    return self.title
    