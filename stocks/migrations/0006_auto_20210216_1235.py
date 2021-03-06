# Generated by Django 3.1.5 on 2021-02-16 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_auto_20210204_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='industries',
            name='slug',
            field=models.SlugField(default=models.CharField(db_column='Industry', max_length=100, unique=True), max_length=255),
        ),
        migrations.AddField(
            model_name='sectors',
            name='slug',
            field=models.SlugField(default=models.CharField(db_column='Sector', max_length=100, unique=True), max_length=255),
        ),
        migrations.AlterField(
            model_name='industries',
            name='sector',
            field=models.ForeignKey(db_column='Sector', on_delete=django.db.models.deletion.CASCADE, related_name='industries', to='stocks.sectors', to_field='sector'),
        ),
        migrations.AlterField(
            model_name='tickers',
            name='industry',
            field=models.ForeignKey(db_column='Industry', on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='stocks.industries', to_field='industry'),
        ),
    ]
