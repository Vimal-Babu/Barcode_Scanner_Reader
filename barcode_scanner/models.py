from django.db import models

# Create your models here.
from django.db import models

class Barcode(models.Model):
    image = models.ImageField(upload_to="barcodes/")
    data = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data
