from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    ISBN=models.CharField(max_length=13,unique=True)
    name=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Publisher=models.CharField(max_length=50)
    Publication_date=models.DateField()
    Genres=models.CharField(max_length=50)
    Print_length=models.PositiveSmallIntegerField()
    is_avaible=models.BooleanField(default=True)



    def __str__(self) -> str:
        return f'{self.name} by {self.Author}'

    @property
    def takedBy(self):
        return self.borrow_book.user.username
    
        


class Borrow(models.Model):
    Book=models.OneToOneField(Book,on_delete=models.CASCADE,related_name='borrow_book')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='borrow_user')


    def __str__(self) -> str:
        return f'{self.Book.name} borrowed by {self.user.username}'