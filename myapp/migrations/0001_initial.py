# Generated by Django 4.0.6 on 2022-08-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.CharField(default='', max_length=20)),
                ('Address', models.CharField(default='', max_length=20)),
                ('Contact', models.IntegerField(default='')),
                ('Mail', models.CharField(default='', max_length=20)),
                ('image', models.ImageField(upload_to='imges/')),
            ],
        ),
    ]
