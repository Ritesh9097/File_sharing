# Generated by Django 3.1.6 on 2021-05-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Enter your file name', max_length=50)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('File_type', models.CharField(default='pdf', max_length=50)),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
