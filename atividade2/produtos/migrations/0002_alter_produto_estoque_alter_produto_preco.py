# Generated by Django 5.1.4 on 2025-01-03 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço'),
        ),
    ]
