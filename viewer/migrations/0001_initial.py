# Generated by Django 4.2.2 on 2023-06-21 17:20

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
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('birth_date', models.DateField(null=True)),
                ('country', models.CharField(max_length=32, null=True)),
            ],
            options={
                'ordering': ['name', 'birth_date'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('original_name', models.CharField(max_length=64)),
                ('year', models.PositiveIntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField()),
                ('page', models.PositiveIntegerField()),
                ('isbn', models.CharField(max_length=32)),
                ('amount', models.PositiveIntegerField()),
                ('author', models.ManyToManyField(to='viewer.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Genres',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_to', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rented',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateField(blank=True)),
                ('reservation_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True)),
                ('id_book', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='viewer.book')),
                ('id_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='viewer.person')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id_book', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='viewer.book')),
                ('id_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='viewer.person')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id_book', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='viewer.book')),
                ('id_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='viewer.person')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='viewer.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(to='viewer.language'),
        ),
    ]