from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Book,Borrow

class BorrowSerializer(serializers.ModelSerializer):
    
    user=serializers.SlugRelatedField(
        queryset=User.objects.filter(),
        read_only=False,
        slug_field='username'
     )
    Book=serializers.SlugRelatedField(
        queryset=Book.objects.filter(),
        read_only=False,
        slug_field='name'
     )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    _comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'ISBN', 'image', 'name', 'Author', 'Publisher',
                  'Publication_date', 'Genres', 'Print_length', '_likes_count', '_comments']


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

class BorrowBookSerializer(serializers.ModelSerializer):
    
    name=serializers.SlugRelatedField(
        queryset=Book.objects.filter(),
        read_only=False,
        slug_field='name',
        source='Book'
     )
    book_id=serializers.SlugRelatedField(
        queryset=Book.objects.filter(),
        read_only=False,
        slug_field='id',
        source='Book'
     )

    class Meta:
        model=Borrow
        fields=['book_id','name']



class UserSerializer(serializers.ModelSerializer):
    borrow_books=BorrowBookSerializer(many=True,read_only=True,source='borrow_user')

    class Meta:
        model=User
        fields=['id','username','email','borrow_books']
