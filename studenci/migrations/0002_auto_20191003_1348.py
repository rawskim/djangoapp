# Generated by Django 2.2.5 on 2019-10-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studenci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dochod',
            field=models.DecimalField(decimal_places=2, default=0, max_digits='6'),
        ),
        migrations.AlterField(
            model_name='student',
            name='roks',
            field=models.CharField(blank=True, default='', max_length=3, verbose_name='rok studiów'),
        ),
    ]
