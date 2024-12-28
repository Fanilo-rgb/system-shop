from django.db import models

# Create your models here.

class Distributeur(models.Model):
    GENDER = (
        ("M", "Masculin"),
        ("F", "Feminin"),
    )
    card_id = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=1, choices=GENDER)
    nationality = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    cin = models.CharField(max_length=12, null=True, blank=True)
    phone_number = models.CharField(max_length=9)
    adress = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=3)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    person = models.ForeignKey(Distributeur, on_delete=models.CASCADE, related_name="invoices")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person.card_id} {self.person.name}"


class Invoice_Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price
    
    def total_ar(self):
        return (self.quantity * self.product.price) * 3600
    
    def __str__(self):
        return str(f"{self.invoice.person.name} {self.invoice.created_at}")
