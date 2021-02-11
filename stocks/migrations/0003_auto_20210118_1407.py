# Generated by Django 3.1.5 on 2021-01-18 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_tickersaggregate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultsyearly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enddate', models.DateField(db_column='EndDate')),
                ('cfoperations', models.DecimalField(db_column='cfOperations', decimal_places=2, max_digits=15)),
                ('dividendspaid', models.DecimalField(db_column='DividendsPaid', decimal_places=2, max_digits=15)),
                ('stockissuance', models.DecimalField(db_column='StockIssuance', decimal_places=2, max_digits=15)),
                ('totalassets', models.DecimalField(db_column='TotalAssets', decimal_places=2, max_digits=15)),
                ('totallongtermdebt', models.DecimalField(db_column='TotalLongTermDebt', decimal_places=2, max_digits=15)),
                ('totalcurrentassets', models.DecimalField(db_column='TotalCurrentAssets', decimal_places=2, max_digits=15)),
                ('totalcurrentliabilities', models.DecimalField(db_column='TotalCurrentLiabilities', decimal_places=2, max_digits=15)),
                ('totalrevenue', models.DecimalField(db_column='TotalRevenue', decimal_places=2, max_digits=15)),
                ('netincomecontinuingops', models.DecimalField(db_column='NetIncomeContinuingOps', decimal_places=2, max_digits=15)),
                ('publicationdate', models.DateField(blank=True, db_column='PublicationDate', null=True)),
                ('margin', models.DecimalField(blank=True, db_column='Margin', decimal_places=2, max_digits=15, null=True)),
                ('leverage', models.DecimalField(blank=True, db_column='Leverage', decimal_places=2, max_digits=15, null=True)),
                ('liquidity', models.DecimalField(blank=True, db_column='Liquidity', decimal_places=2, max_digits=15, null=True)),
                ('cfpositive', models.IntegerField(blank=True, db_column='cfPositive', null=True)),
                ('nostockissuance', models.IntegerField(blank=True, db_column='noStockIssuance', null=True)),
                ('cfaboveincome', models.IntegerField(blank=True, db_column='cfAboveIncome', null=True)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.tickers')),
            ],
            options={
                'db_table': 'resultsyearly',
                'managed': True,
                'unique_together': {('ticker', 'enddate')},
            },
        ),
        migrations.DeleteModel(
            name='Rawdatayearly',
        ),
    ]