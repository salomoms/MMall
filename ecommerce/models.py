from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d')
    price = models.DecimalField(decimal_places=2, max_digits=24, default=0)
    description = models.TextField(max_length=255, blank=True)
    brand = models.ForeignKey(Brand)
    category = models.ForeignKey('Category')
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return "%s (%s) - %s" % (self.title, self.brand.name, self.category.name)


class Category(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey("self", related_name="children", blank=True, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    address = models.TextField(blank=False)
    birth_date = models.DateField(blank=False)
    password = models.TextField(blank=False)
    gender = models.CharField(blank=False, choices=(('Co', 'Cowok'),('Ce','Cewek')), max_length=2)


class Cart(models.Model):
    delivery_name = models.CharField(max_length=30)
    delivery_address = models.TextField(blank=True, default='')
    payment_method = models.CharField(blank=True, max_length=20, default='', choices=(('ngutang', 'Ngutang'), ('cod', 'Cash On Delivery')))
    paid = models.BooleanField(default=False)
    total_discout = models.FloatField(default=0)
    created_by = models.ForeignKey(Customer)

    def __str__(self):
        return 'Order #%d a/n %s ' % (self.id, self.delivery_name)


class CartItem(models.Model):
    product = models.ForeignKey(Product)
    items = models.IntegerField(default=1)
    discount_per_product = models.FloatField(default=0)
    cart = models.ForeignKey(Cart)

    def __str__(self):
        return self.product.title
