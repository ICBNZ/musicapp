# Generated by Django 2.1.5 on 2019-03-02 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190302_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='extra_pic',
        ),
        migrations.AddField(
            model_name='student',
            name='second_inst',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='second_inst',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
