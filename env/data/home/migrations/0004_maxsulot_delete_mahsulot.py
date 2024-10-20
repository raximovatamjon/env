# Generated by Django 4.2.7 on 2023-12-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_mahsulot'),
    ]

    operations = [
        migrations.CreateModel(
            name='maxsulot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='mahsulot',
        ),
    ]
