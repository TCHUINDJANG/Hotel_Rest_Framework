from django.db import models
import uuid

# Create your models here.
class Hotels(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    name = models.IntegerField()
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'api_hotels'

class User(models.Model):
    pass
