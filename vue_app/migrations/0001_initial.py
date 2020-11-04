# Generated by Django 3.1.1 on 2020-10-02 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=60)),
                ('subject_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('due_date', models.DateTimeField(verbose_name='date deadline')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vue_app.subject')),
            ],
        ),
    ]