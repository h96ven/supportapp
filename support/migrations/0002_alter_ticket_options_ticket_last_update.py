# Generated by Django 4.0.5 on 2022-06-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='ticket',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
