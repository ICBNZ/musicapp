# Generated by Django 2.1.5 on 2019-03-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190302_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hour',
            name='day_of_week',
            field=models.CharField(choices=[('Monday', 'Mon'), ('Tuesday', 'Tues'), ('Wednesday', 'Wed'), ('Thursday', 'Thurs'), ('Friday', 'Fri'), ('Saturday', 'Sat'), ('Sunday', 'Sun')], default=1, max_length=10),
        ),
    ]
