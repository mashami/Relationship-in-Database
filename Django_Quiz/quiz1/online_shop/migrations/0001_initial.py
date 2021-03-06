# Generated by Django 4.0.6 on 2022-07-06 19:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id_account', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('billing_address', models.CharField(max_length=100, null=True)),
                ('isclosed', models.BooleanField()),
                ('open', models.DateTimeField(auto_now_add=True)),
                ('closed', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ordered', models.DateTimeField(auto_now_add=True)),
                ('shipped', models.DateField()),
                ('total', models.IntegerField()),
                ('ship_to', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('NEW', 'new'), ('HOLD', 'hold'), ('SHIPPER', 'shipper'), ('DELIVERED', 'delived'), ('CLOSED', 'closed')], max_length=100, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_order', to='online_shop.account')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('supplier', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Web_user',
            fields=[
                ('log_in', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
                ('state', models.CharField(choices=[('NEW', 'new'), ('ACTIVE', 'active'), ('BLOCKED', 'blocked'), ('BANNER', 'banner')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shopping_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_Date', models.DateField(auto_now_add=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account_shop', to='online_shop.account')),
                ('webUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_web', to='online_shop.web_user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id_payment', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('paid', models.DateField(auto_now_add=True)),
                ('total_payment', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_payment', to='online_shop.account')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_payment', to='online_shop.order')),
            ],
        ),
        migrations.CreateModel(
            name='line_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_line_item', to='online_shop.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_line_item', to='online_shop.product')),
                ('shoping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_line_item', to='online_shop.shopping_cart')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone', models.IntegerField()),
                ('web', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_web', to='online_shop.web_user')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_account', to='online_shop.customer'),
        ),
    ]
