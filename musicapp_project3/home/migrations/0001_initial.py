# Generated by Django 2.1.5 on 2019-03-02 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availablity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Availability')),
            ],
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(max_length=8)),
                ('day_of_week', models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], default=1, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('details', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('profile_pic', models.ImageField(default='concert.jpg', upload_to='images/')),
                ('extra_pic', models.ImageField(default='concert.jpg', upload_to='images/')),
                ('name', models.CharField(max_length=150)),
                ('about', models.TextField(blank=True, null=True)),
                ('instrument_req', models.BooleanField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('instrument', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Instrument')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('profile_pic', models.ImageField(default='concert.jpg', upload_to='images/')),
                ('extra_pic', models.ImageField(default='concert.jpg', upload_to='images/')),
                ('name', models.CharField(max_length=150)),
                ('experience', models.TextField(blank=True, null=True)),
                ('instrument_avail', models.BooleanField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('instrument', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Instrument')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
        migrations.AddField(
            model_name='availability',
            name='hour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Hour'),
        ),
        migrations.AddField(
            model_name='availability',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Tutor'),
        ),
    ]
