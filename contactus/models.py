from django.db import models

from PIL import Image

from django.utils import timezone

class ContactData(models.Model):
  full_name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  date_entry = models.DateTimeField(default=timezone.now())
  photo = models.ImageField(upload_to='photos/contacts')

  def __str__(self):
    return self.full_name
