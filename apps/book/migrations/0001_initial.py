# Generated by Django 3.0 on 2020-10-21 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.DateField(verbose_name='Release Date')),
                ('cover', models.ImageField(upload_to='cover')),
                ('visits', models.PositiveIntegerField()),
                ('authors', models.ManyToManyField(to='author.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Category')),
            ],
        ),
    ]
