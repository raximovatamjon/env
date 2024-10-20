# Generated by Django 5.0 on 2023-12-07 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='maxsulot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('desciption', models.TextField()),
                ('category', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='image')),
                ('date', models.DateField()),
            ],
        ),
    ]
