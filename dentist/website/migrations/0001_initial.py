# Generated by Django 3.0.7 on 2020-06-22 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='get_in_touch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('massage_name', models.CharField(max_length=20)),
                ('massage_Email', models.EmailField(max_length=50)),
                ('massage', models.TextField()),
            ],
        ),
    ]