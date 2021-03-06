# Generated by Django 2.2.2 on 2019-06-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("klanad", "0007_auto_20190607_0630")]

    operations = [
        migrations.AlterModelOptions(
            name="productgroup", options={"ordering": ("position",)}
        ),
        migrations.AddField(
            model_name="productgroup",
            name="archived",
            field=models.BooleanField(
                default=False,
                help_text="ProductGroups which are archived are not shown.",
            ),
        ),
        migrations.AddField(
            model_name="productgroup",
            name="position",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="The order in which product groups are shown, in ascending order.",
                null=True,
            ),
        ),
    ]
