# Generated by Django 4.0.4 on 2022-05-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_paidbooking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paidbooking',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
