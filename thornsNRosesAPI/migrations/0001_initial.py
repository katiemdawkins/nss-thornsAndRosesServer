# Generated by Django 4.0.6 on 2022-07-17 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=25)),
                ('markup_percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=25)),
                ('species', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=150)),
                ('markup_percentage', models.IntegerField()),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thornsNRosesAPI.distributor')),
            ],
        ),
        migrations.CreateModel(
            name='NurseryFlowerPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thornsNRosesAPI.distributor')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thornsNRosesAPI.flower')),
                ('nursery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thornsNRosesAPI.nursery')),
            ],
        ),
    ]
