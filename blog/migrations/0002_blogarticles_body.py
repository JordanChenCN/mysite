# Generated by Django 2.2.4 on 2019-08-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticles',
            name='body',
            field=models.TextField(default=0),
        ),
    ]