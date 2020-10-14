# Generated by Django 3.1.2 on 2020-10-14 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yalla_business_app', '0004_auto_20201014_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=64)),
                ('store_location', models.TextField()),
                ('store_pic', models.CharField(max_length=64)),
                ('comment', models.TextField()),
                ('review_rate', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]