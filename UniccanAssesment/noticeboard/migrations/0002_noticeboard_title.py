# Generated by Django 2.2 on 2019-11-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticeboard',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
