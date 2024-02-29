# Generated by Django 5.0.1 on 2024-01-20 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostilas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewApostila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('apostila', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apostilas.apostila')),
            ],
        ),
    ]
