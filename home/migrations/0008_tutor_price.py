# Generated by Django 2.1.5 on 2019-02-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190220_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
