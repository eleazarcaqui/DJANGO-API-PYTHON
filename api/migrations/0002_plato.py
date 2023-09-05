# Generated by Django 3.2 on 2023-09-02 02:47

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('plato_id', models.AutoField(primary_key=True, serialize=False)),
                ('plato_nom', models.CharField(max_length=200, verbose_name='Nombre')),
                ('plato_img', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image')),
                ('plato_pre', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio')),
                ('categoria_id', models.ForeignKey(db_column='categoria_id', on_delete=django.db.models.deletion.RESTRICT, related_name='Platos', to='api.categoria', verbose_name='Categoria')),
            ],
            options={
                'db_table': 'tbl_plato',
            },
        ),
    ]
