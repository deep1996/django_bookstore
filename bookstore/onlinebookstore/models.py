from django.db import models


class books(models.Model):
      book_id=models.IntegerField()
      book_name=models.CharField(max_length=30)
      book_author=models.CharField(max_length=50)
      book_price=models.CharField(max_length=10)
      book_section=models.CharField(max_length=10)

