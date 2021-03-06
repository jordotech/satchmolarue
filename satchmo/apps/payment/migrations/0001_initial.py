# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-29 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_shipping_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCardDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_type', models.CharField(choices=[(b'visa', 'Visa'), (b'mastercard', 'Mastercard'), (b'discover', 'Discover'), (b'amex', 'American Express')], max_length=16, verbose_name='Credit Card Type')),
                ('display_cc', models.CharField(max_length=4, verbose_name='CC Number (Last 4 digits)')),
                ('encrypted_cc', models.CharField(blank=True, editable=False, max_length=40, null=True, verbose_name='Encrypted Credit Card')),
                ('expire_month', models.IntegerField(verbose_name='Expiration Month')),
                ('expire_year', models.IntegerField(verbose_name='Expiration Year')),
                ('card_holder', models.CharField(blank=True, max_length=60, verbose_name='card_holder Name')),
                ('start_month', models.IntegerField(blank=True, null=True, verbose_name='Start Month')),
                ('start_year', models.IntegerField(blank=True, null=True, verbose_name='Start Year')),
                ('issue_num', models.CharField(blank=True, max_length=2, null=True)),
                ('orderpayment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditcards', to='shop.OrderPayment', unique=True)),
            ],
            options={
                'verbose_name': 'Credit Card',
                'verbose_name_plural': 'Credit Cards',
            },
        ),
        migrations.CreateModel(
            name='PaymentOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20, verbose_name='Description')),
                ('active', models.BooleanField(default=False, help_text='Should this be displayed as an option for the user?', verbose_name='Active')),
                ('optionName', models.CharField(choices=[('GIFT_CARDS', 'Gift Card'), ('AUTHNET', 'Credit Card')], help_text='The class name as defined in payment.py', max_length=20, unique=True, verbose_name='Option Name')),
                ('sortOrder', models.IntegerField(verbose_name='Sort Order')),
            ],
            options={
                'verbose_name': 'Payment Option',
                'verbose_name_plural': 'Payment Options',
            },
        ),
    ]
