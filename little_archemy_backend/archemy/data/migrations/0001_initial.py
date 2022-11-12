# Generated by Django 4.0.5 on 2022-11-12 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=6000)),
                ('credits', models.IntegerField(null=True)),
                ('prime', models.BooleanField()),
                ('parents', models.ManyToManyField(to='archemy.item')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=40)),
                ('admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemMirror',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=6000)),
                ('aprove', models.CharField(max_length=60)),
                ('desaprove', models.CharField(max_length=6000)),
                ('parents', models.ManyToManyField(related_name='childs', to='archemy.item')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_mirror', to='archemy.user')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='archemy.user'),
        ),
    ]
