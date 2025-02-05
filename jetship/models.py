from django.db import models
from django.utils import timezone



# Custom User Model (Guest)
class Guest(models.Model):
    phone_number = models.CharField(max_length=13, unique=True)
    uuid = models.CharField(max_length=36, unique=True)
    role = models.CharField(max_length=20, default='guest')    
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.TextField()
    village = models.CharField(max_length=30)
    taluka = models.CharField(max_length=30)
    district = models.CharField(max_length=30)     
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone_number

# Driver Model
class Driver(models.Model):
    user = models.OneToOneField(Guest, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=15)
    experience_years = models.PositiveIntegerField()
    aadhar_number = models.CharField(max_length=12)
    type_of_driver = models.CharField(max_length=20)
    images = models.JSONField(default=dict)

    def __str__(self):
        return f"Driver: {self.user.name}"


class Category(models.Model):
    category = models.CharField(max_length=255)
    category_link = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.category

class Subcategory(models.Model):
    subcategory = models.CharField(max_length=255)
    subcategory_link = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.subcategory

class Post(models.Model):
    user = models.ForeignKey(Guest, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Change to ForeignKey
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_category = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    whatsapp_no = models.CharField(max_length=15)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    images = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        indexes = [
            models.Index(fields=['-created_at'])  # Correct way to index
        ]

