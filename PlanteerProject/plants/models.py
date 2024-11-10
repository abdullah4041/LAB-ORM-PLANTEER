from django.db import models

# Create your models here.

class Plant(models.Model):
    '''
    name 
    about
    used_for
    image
    category
    is_edible
    created_at

    '''
    class Category(models.TextChoices):
        HERB = 'herb', 'Herb'
        TREE = 'tree', 'Tree'
        VEGETABLES= 'vegetables', 'Vegetables'
        FRULT ='frult' ,'Frult'
        FLOWER = 'flower', 'Flower'

    name = models.CharField(max_length=50)
    about = models.TextField()
    used_for =models.TextField()
    image =models.ImageField(upload_to='images/')
    category = models.CharField(
        max_length=10,
        choices=Category.choices,
        default=Category.TREE
    )
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
