# Generated by Django 4.1 on 2022-09-16 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(max_length=20)),
                ('balance', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_of_origin', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.TextField(default='')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.CharField(max_length=20)),
                ('loan_type', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('interest', models.IntegerField()),
                ('loan_term', models.IntegerField()),
                ('payment_due_date', models.DateTimeField()),
                ('loan_balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(max_length=6)),
                ('receipt_date', models.DateTimeField()),
                ('transaction', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('receipt_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.BigIntegerField()),
                ('date_of_reward', models.DateTimeField()),
                ('transaction_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=13)),
                ('user_email', models.EmailField(max_length=254)),
                ('account_number', models.CharField(max_length=15)),
                ('account_name', models.CharField(max_length=20)),
                ('balance', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
                ('pin', models.IntegerField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_currency', to='wallet.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(max_length=40)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=20)),
                ('transaction_charge', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('message', models.CharField(max_length=20, null=True)),
                ('destination_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions_destination', to='wallet.wallet')),
                ('origin_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions_origin', to='wallet.wallet')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('transaction_cost', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_third_party', to='wallet.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_party_currency', to='wallet.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.TextField()),
                ('title', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateTimeField()),
                ('recepients', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_recepients', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('card_name', models.CharField(max_length=20)),
                ('expiry_date', models.DateTimeField()),
                ('security_code', models.CharField(max_length=20)),
                ('card_type', models.CharField(max_length=20)),
                ('date_issue', models.DateTimeField()),
                ('issuer', models.CharField(max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_account', to='wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Account_currency', to='wallet.wallet'),
        ),
    ]
