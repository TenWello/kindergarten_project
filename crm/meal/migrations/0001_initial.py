# Generated by Django 5.2.1 on 2025-05-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_rename_cost_product_total_cost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('portion', models.DateTimeField(auto_now_add=True)),
                ('cooking_time', models.DurationField(blank=True, null=True)),
                ('recipe', models.TextField(blank=True, null=True)),
                ('ingredient', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('products', models.ManyToManyField(to='product.product')),
            ],
        ),
    ]
