# Generated by Django 4.1.7 on 2023-07-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=50, null=True)),
                ('cimage', models.ImageField(blank=True, null=True, upload_to='categoryImage')),
                ('members', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('mobileno', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
