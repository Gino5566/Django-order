# Generated by Django 4.2.1 on 2023-05-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0008_remove_order_shopping_cart_order_shopping_cart_items"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total",
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]
