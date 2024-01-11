from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import CustomUser


class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    isbn=models.CharField(max_length=17)

    def __str__(self):
        return self.title


class BookImage(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="images")
    book_image=models.ImageField(upload_to='images_book/')


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    bio=models.TextField()


class BookAuthor(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)



class BookReview(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    comment=models.TextField()
    stars=models.IntegerField(
        validators=[
            MinValueValidator(1,message="baho 1 dan kam bo'lmasligi kerak"),
            MaxValueValidator(5,message="baho 5 dan ko'p bo'lmasligi kerak")

        ]
    )

