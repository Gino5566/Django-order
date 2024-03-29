# Generated by Django 4.2.1 on 2023-05-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0003_option_food_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="food", old_name="food_text", new_name="name",
        ),
        migrations.RemoveField(model_name="food", name="pub_date",),
        migrations.AddField(
            model_name="food",
            name="price",
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]
