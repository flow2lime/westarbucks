# Generated by Django 3.2.4 on 2021-08-15 15:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alg_milk', models.BooleanField(default=False)),
                ('alg_bean', models.BooleanField(default=False)),
                ('alg_egg', models.BooleanField(default=False)),
                ('alg_wheat', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'allergies',
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='english_name',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='Delicious!', max_length=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='korean_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serving_kcal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=6)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sugar_g', models.DecimalField(decimal_places=2, max_digits=6)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=6)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size_ml', models.CharField(max_length=20)),
                ('size_fluid_ounce', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='allergies',
            field=models.ManyToManyField(related_name='products', to='products.Allergy'),
        ),
    ]
