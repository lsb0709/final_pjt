from django.db import models

# from accounts.models import Pet
# from care.models import Care, Review
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# class Dogwalking(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
#     )
#     pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
#     condition = models.ForeignKey(Care, on_delete=models.CASCADE)
#     grade = models.ForeignKey(Review, on_delete=models.CASCADE)
#     location = models.TextField()


# class Review(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
#     )
#     content = models.TextField()
#     grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])