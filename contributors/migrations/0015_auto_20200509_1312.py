# Generated by Django 3.0.6 on 2020-05-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0014_auto_20200508_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='createcontributor',
            name='about_you',
            field=models.TextField(default='working as software developer'),
        ),
        migrations.AddField(
            model_name='createcontributor',
            name='profession',
            field=models.CharField(default='Developer', max_length=255),
        ),
    ]