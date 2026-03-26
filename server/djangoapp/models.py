from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.

# DealerReview model for reviews per dealer
class DealerReview(models.Model):
	dealer_id = models.IntegerField()
	reviewer = models.CharField(max_length=100)
	review = models.TextField()
	rating = models.IntegerField(default=5)
	created_at = models.DateTimeField(default=now)

	def __str__(self):
		return f"Review by {self.reviewer} for dealer {self.dealer_id}: {self.review[:30]}..."

# Dealer model for all dealers
class Dealer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.city}, {self.state})"


# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Car Model model
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'WAGON'
    COUPE = 'Coupe'
    HATCHBACK = 'Hatchback'
    CONVERTIBLE = 'Convertible'
    BODY_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (HATCHBACK, 'Hatchback'),
        (CONVERTIBLE, 'Convertible'),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES)
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"
