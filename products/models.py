from django.db import models
from django.db.models.deletion import CASCADE

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name  = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    allergies    = models.ManyToManyField('Allergy', related_name='products')

    class Meta:
        db_table = 'products'
        
class Images(models.Model):
    img_url = models.URLField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Nutrition(models.Model):
    serving_kcal     = models.DecimalField(max_digits=6, decimal_places=2)
    sodium_mg        = models.DecimalField(max_digits=6, decimal_places=2)
    saturated_fat_g  = models.DecimalField(max_digits=6, decimal_places=2)
    sugar_g          = models.DecimalField(max_digits=6, decimal_places=2)
    protein_g        = models.DecimalField(max_digits=6, decimal_places=2)
    caffeine_mg      = models.DecimalField(max_digits=6, decimal_places=2)
    size_ml          = models.CharField(max_length=20)
    size_fluid_ounce = models.CharField(max_length=20)
    product          = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'

class Allergy(models.Model):
    alg_milk  = models.BooleanField(default=False)
    alg_bean  = models.BooleanField(default=False)
    alg_egg   = models.BooleanField(default=False)
    alg_wheat = models.BooleanField(default=False)

    class Meta:
        db_table = 'allergies'


