# Generated by Django 4.0.6 on 2022-08-04 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0012_alter_ticket_options_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['-updated_at']},
        ),
    ]
