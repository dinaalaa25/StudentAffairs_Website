# Generated by Django 4.0.4 on 2022-05-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_add_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='dateofbirth',
            field=models.DateField(),
        ),
    ]
