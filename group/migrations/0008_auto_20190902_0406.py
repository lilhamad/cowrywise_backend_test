# Generated by Django 2.2.4 on 2019-09-02 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0007_auto_20190902_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(default='1', editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
