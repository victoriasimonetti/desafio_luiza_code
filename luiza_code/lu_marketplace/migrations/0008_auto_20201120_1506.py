# Generated by Django 3.1.3 on 2020-11-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lu_marketplace', '0007_auto_20201120_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='prod_descricao',
            field=models.TextField(max_length=100, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='prod_nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
    ]