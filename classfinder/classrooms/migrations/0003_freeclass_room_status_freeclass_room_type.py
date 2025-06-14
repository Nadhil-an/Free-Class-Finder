# Generated by Django 5.2.1 on 2025-05-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0002_alter_freeclass_free_day_alter_freeclass_free_hour_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='freeclass',
            name='room_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Occupied', 'Occupied')], default=False, max_length=20),
        ),
        migrations.AddField(
            model_name='freeclass',
            name='room_type',
            field=models.CharField(choices=[('classroom', 'Classroom'), ('Computer Lab', 'Computer Lab')], default='Available', max_length=20),
            preserve_default=False,
        ),
    ]
