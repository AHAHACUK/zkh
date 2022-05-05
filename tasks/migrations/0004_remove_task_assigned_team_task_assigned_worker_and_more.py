# Generated by Django 4.0.4 on 2022-05-05 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_worker_team'),
        ('tasks', '0003_remove_report_image_reportimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_team',
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='accounts.worker'),
        ),
        migrations.AlterField(
            model_name='report',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='tasks.task'),
        ),
        migrations.AlterField(
            model_name='reportimage',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tasks.report'),
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
