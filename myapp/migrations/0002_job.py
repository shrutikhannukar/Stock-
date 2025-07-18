# Generated by Django 5.1.4 on 2024-12-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('Junior', 'Junior'), ('Senior', 'Senior'), ('Internship', 'Internship')], max_length=50)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Contract', 'Contract')], max_length=50)),
                ('company_name', models.CharField(max_length=255)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
                ('description', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
