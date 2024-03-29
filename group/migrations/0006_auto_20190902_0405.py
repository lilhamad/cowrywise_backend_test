# Generated by Django 2.2.4 on 2019-09-02 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0005_auto_20190902_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payer',
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(default='0', editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='payment',
            name='group',
        ),
        migrations.AddField(
            model_name='payment',
            name='group',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
    ]
