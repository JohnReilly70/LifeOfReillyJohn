# Generated by Django 2.1.7 on 2019-05-31 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LifeOfReillyJohnApp', '0002_auto_20190531_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='Type1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='Type2',
            field=models.CharField(max_length=50),
        ),
    ]
