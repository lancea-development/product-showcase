# Generated by Django 2.2.2 on 2019-06-07 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("klanad", "0006_auto_20190606_1220")]

    operations = [
        migrations.AlterField(
            model_name="productgroup",
            name="title",
            field=models.CharField(
                help_text="The name of the product group.", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="productgroupimage",
            name="image",
            field=models.ImageField(upload_to="product-groups"),
        ),
    ]
