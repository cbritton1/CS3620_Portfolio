from django.db import models


# Create your models here.
class Hobby(models.Model):
    def __str__(self):
        item = self.item_name + ': ' + self.item_desc + '; '
        return item

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_image = models.CharField(max_length=500, default="https://image.freepik.com/free-icon/skiing_318-9893.jpg")


class Portfolio(models.Model):
    def __str__(self):
        item = self.item_name + ': ' + self.item_desc + '; '
        return item
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_image = models.CharField(max_length=500, default="https://oceanwp.org/wp-content/uploads/2017/07/portfolio-image.png")


class Contact(models.Model):
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_message = models.TextField()
