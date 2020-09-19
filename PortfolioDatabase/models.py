from django.db import models


# Create your models here.
class Hobby(models.Model):

    def __str__(self):
        item = self.item_name + ': ' + self.item_desc + '; '
        return item

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)


class Portfolio(models.Model):
    def __str__(self):
        item = self.item_name + ': ' + self.item_desc + '; '
        return item
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
