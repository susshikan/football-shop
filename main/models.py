from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('match_worn_vintage', 'Match Worn Vintage'),
        ('player_issue_vintage', 'Player Issue Vintage'),
        ('replica_vintage', 'Replica Vintage'),
        ('reissue_retro', 'Reissue Retro'),
        ('special_edition_vintage', 'Special Edition Vintage'),
        ('analysis', 'Analysis'),
    ]

    history_value_choices = [
        ('classic', 'Classic'),
        ('signed_vintage', 'Signed Vintage'),
        ('limited_edition', 'Limited Edition'),
        ('historical_matches', 'Historical Matches')
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='match_worn_vintage')
    is_featured = models.BooleanField(default=False)
    season = models.CharField(max_length=9)
    exlusive = models.BooleanField(default=False)
    history_value = models.CharField(max_length=50, choices=history_value_choices, default='classic')

    def __str__(self):
        return self.name
