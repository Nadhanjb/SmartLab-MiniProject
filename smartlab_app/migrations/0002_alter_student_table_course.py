# Generated by Django 3.2.22 on 2023-10-24 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartlab_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_table',
            name='COURSE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartlab_app.course_table'),
        ),
    ]
