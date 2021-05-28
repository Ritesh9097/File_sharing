# Generated by Django 3.1.6 on 2021-05-24 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('last_download', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Enter your file name', max_length=50)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('extension', models.CharField(default='pdf', max_length=50)),
                ('path', models.FileField(upload_to='uploads/', verbose_name='select file')),
                ('size', models.FloatField(default=0.0, verbose_name='filesize')),
            ],
        ),
        migrations.DeleteModel(
            name='Uploadform',
        ),
        migrations.AddField(
            model_name='download',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.file', verbose_name='file name'),
        ),
    ]