# Generated by Django 5.0.2 on 2024-07-17 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_alter_appointment_patient'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
