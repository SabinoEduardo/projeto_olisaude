# Generated by Django 4.2.7 on 2023-11-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olisaude', '0003_alter_costumer_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
