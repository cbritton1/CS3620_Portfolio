# Generated by Django 3.1.1 on 2020-09-29 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0003_auto_20200928_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='item_image',
            field=models.CharField(default='https://oceanwp.org/wp-content/uploads/2017/07/portfolio-image.png', max_length=500),
        ),
    ]
