from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(blank = False, max_length = 50)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(blank = False, max_length = 50)

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    pageCount = models.IntegerField(blank=False)
    genre = models.ForeignKey(Genre, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    tags = models.ManyToManyField(Tags)
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=80)
    last_name = models.CharField(blank=False, max_length=80)
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

