# Generated by Django 2.2.6 on 2019-10-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_auto_20191003_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name_plural': 'pizze'},
        ),
        migrations.AlterModelOptions(
            name='skladnik',
            options={'verbose_name_plural': 'skladniki'},
        ),
        migrations.AlterField(
            model_name='skladnik',
            name='pizze',
            field=models.ManyToManyField(blank=True, null=True, related_name='skladniki', to='pizza.Pizza'),
        ),
    ]
