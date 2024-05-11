# Generated by Django 4.2.11 on 2024-05-11 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_remove_attractions_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attractionimage",
            name="attraction",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attraction_images",
                to="core.attractions",
                verbose_name="картинки",
            ),
        ),
    ]
