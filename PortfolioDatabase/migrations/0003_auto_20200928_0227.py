# Generated by Django 3.1.1 on 2020-09-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0002_hobby_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='item_image',
            field=models.CharField(default='https://image.freepik.com/free-icon/skiing_318-9893.jpg', max_length=500),
        ),
    ]
