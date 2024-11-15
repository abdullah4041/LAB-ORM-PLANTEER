# Generated by Django 5.1.2 on 2024-11-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('used_for', models.TextField()),
                ('image', models.ImageField(upload_to='plants/')),
                ('category', models.CharField(choices=[('herb', 'Herb'), ('tree', 'Tree'), ('shrub', 'Shrub'), ('flower', 'Flower')], default='herb', max_length=10)),
                ('is_edible', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
