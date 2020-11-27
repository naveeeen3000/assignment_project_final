# Generated by Django 3.1.3 on 2020-11-26 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('question', models.TextField()),
                ('question_file', models.FileField(blank=True, default=None, upload_to='')),
                ('deadline_date', models.DateField(null=True)),
                ('deadline_time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.FileField(upload_to='assignments')),
                ('submitted_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='assignment_info.course')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
