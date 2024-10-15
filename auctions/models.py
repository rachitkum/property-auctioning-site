# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils import timezone
# from django.core.validators import MinValueValidator, MaxValueValidator
# import datetime

# class User(AbstractUser):
#     pass

# class Listing(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
#     address = models.CharField(max_length=200, default='default address')
#     size = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
#     year_built = models.IntegerField(
#         validators=[
#             MinValueValidator(1000), 
#             MaxValueValidator(datetime.datetime.now().year)
#         ],
#         default=datetime.datetime.now().year
#     )
#     tags = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title

# class ListingImage(models.Model):
#     listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='listing_images/')

#     def __str__(self):
#         return f"Image for {self.listing.title}"

# class Bid(models.Model):
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
#     bidder = models.ForeignKey(User, on_delete=models.CASCADE)
#     bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     bid_time = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.bidder.username} - {self.bid_amount}"



from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200, default='default address')
    size = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    year_built = models.IntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(datetime.datetime.now().year)
        ],
        default=datetime.datetime.now().year
    )
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listing_images/')

    def __str__(self):
        return f"Image for {self.listing.title}"

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.bidder.username} - {self.bid_amount}"
