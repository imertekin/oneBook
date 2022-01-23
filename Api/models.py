from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    ISBN=models.CharField(max_length=13,unique=True)
    image=models.ImageField(null=True,blank=True,upload_to='%Y/%m/%d')
    name=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Publisher=models.CharField(max_length=50)
    Publication_date=models.DateField()
    Genres=models.CharField(max_length=50)
    Print_length=models.PositiveSmallIntegerField()



    def __str__(self) -> str:
        return f'{self.name} by {self.Author}'

    @property
    def _likes_count(self):
        return self.like.count()

    @property
    def _comments(self):
        return self.books_comment
    
        


class Like(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='like')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker')
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.book.name} liked by {self.user.username}'


class Comment(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='books_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_owner')
    content=models.TextField(max_length=140,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f" {self.user.username} 's comment  "


class Booklist(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='booklist')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Mybooks')
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.book.name} added booklist by {self.user.username}'