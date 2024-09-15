from django.db import models

# Define a Product Category model (if you want to categorize products)
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'Category'

    

  
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()  # To track available stock
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto set when created
    updated_at = models.DateTimeField(auto_now=True)  # Auto update on modification

    class Meta:
        db_table = 'Products'
