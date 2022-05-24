# Generated by Django 4.0.3 on 2022-05-21 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0011_proveedor_categoria_proveedor_subcategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='moda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.categoria'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.subcategoria'),
        ),
    ]