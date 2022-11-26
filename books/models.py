from django.db import models
import uuid
from taggit.managers import TaggableManager


class Book (models.Model):
    cover = models.ImageField(
        default="default_book.png", upload_to="bookcovers/", blank=True, null=True)
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    date_published = models.CharField(max_length=20, null=True)
    publisher = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    pdf_file = models.FileField(upload_to="pdf_files/", null=True, blank=True)
    mp3_file = models.FileField(upload_to="mp3_files/", null=True, blank=True)

    one_star = models.IntegerField(default=0, null=True, blank=True)
    two_star = models.IntegerField(default=0, null=True, blank=True)
    three_star = models.IntegerField(default=0, null=True, blank=True)
    four_star = models.IntegerField(default=0, null=True, blank=True)
    five_star = models.IntegerField(default=0, null=True, blank=True)

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    tags = TaggableManager()

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    book = models.ForeignKey(
        Book, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=16, null=True)
    body = models.TextField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Review of: {self.book} | {self.date_added}"


class Page(models.Model):
    book = models.ForeignKey(
        Book, related_name="pages", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pages/", blank=True, null=True)

    def __str__(self) -> str:
        return f"Page of: {self.book}"
