# Generated by Django 3.0.6 on 2020-05-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0012_auto_20200507_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='createcontributor',
            name='resume',
            field=models.FileField(default=1, upload_to='resumes'),
            preserve_default=False,
        ),
    ]