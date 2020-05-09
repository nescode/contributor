# Generated by Django 3.0.6 on 2020-05-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0013_createcontributor_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createcontributor',
            name='phone',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='createcontributor',
            name='role',
            field=models.CharField(choices=[('developer', 'developer'), ('designer', ' designer'), ('documentation team', 'documentation team')], max_length=25),
        ),
    ]