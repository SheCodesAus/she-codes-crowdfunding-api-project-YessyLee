# Generated by Django 4.1.5 on 2023-01-17 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pledge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pledges', to='projects.project'),
        ),
    ]
