# Generated by Django 2.2.4 on 2019-09-02 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_auto_20190902_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='group',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
    ]