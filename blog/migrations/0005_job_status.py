# Generated by Django 4.1.1 on 2022-10-21 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_job_finishing_alter_job_mark_up_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
