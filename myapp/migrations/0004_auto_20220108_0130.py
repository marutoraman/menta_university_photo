# Generated by Django 3.1.2 on 2022-01-07 16:30

from django.db import migrations, models
import ulid.api.api


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220107_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edituser',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
    ]