# Generated by Django 3.1.2 on 2020-10-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yalla_business_app', '0002_auto_20201018_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='catagories',
            field=models.CharField(choices=[('RE', 'Resturant'), ('CL', 'Clothes'), ('SE', 'Services'), ('BE', 'Beauty'), ('EN', 'Entertainment'), ('ED', 'Education'), ('EL', 'Electrical')], default='ED', max_length=2),
        ),
    ]
