from django.db import models

# Create your models here.
class pmodel(models.Model):
    uid= models.IntegerField(max_length=60)
    state= models.CharField(max_length=10)
    tags= models.CharField(max_length=100)
    img = models.FileField(upload_to='uploads')
    class Meta:
        db_table = "tbl_photo"