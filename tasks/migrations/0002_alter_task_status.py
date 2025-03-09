# Generated by Django 5.1.5 on 2025-03-03 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Upcoming', 'Upcoming'), ('Due Today', 'Due Today'), ('Overdue', 'Overdue')], default='Upcoming', editable=False, max_length=20),
        ),
    ]
