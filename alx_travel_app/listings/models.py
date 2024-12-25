from django.db import models

class Listing(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
	location = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
	listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
	user = models.CharField(max_length=100)
	check_in = models.DateField()
	check_out = models.DateField()
	total_price = models.DecimalField(max_digits=10, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
	listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
	user = models.CharField(max_length=100)
	rating = models.IntegerField()
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
