# Generated by Django 4.0.4 on 2022-06-04 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_project_reason_delete_reasons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.department'),
            preserve_default=False,
        ),
    ]
