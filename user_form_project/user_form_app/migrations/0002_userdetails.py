# Generated by Django 4.2.4 on 2023-08-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_form_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField()),
                ('age', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
