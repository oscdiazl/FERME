# Generated by Django 3.0.5 on 2020-05-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'prod_proveedor',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='ProductoProveedor',
        ),
    ]