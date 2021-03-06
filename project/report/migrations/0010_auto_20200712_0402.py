# Generated by Django 3.0.7 on 2020-07-12 04:02

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0009_auto_20200516_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, help_text='Location of the user when making the Report.', null=True, srid=3857),
        ),
        migrations.AlterField(
            model_name='kmgrid',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, default=None, help_text='Geometry of this grid', null=True, srid=3857),
        ),
        migrations.AlterField(
            model_name='kmgridscore',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, default=None, help_text='Geometry of this Grid', null=True, srid=3857),
        )
    ]
