# Generated by Django 5.0.6 on 2024-10-20 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ege', '0002_category_alter_task_is_used_in_exam'),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ege_category_id', to='ege.category', verbose_name='Category'),
        ),
    ]
