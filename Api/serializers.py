from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Book, Comment, Like


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "password2",
                  "email", "first_name", "last_name")
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True}
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match"})

        return attrs

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )

        user.set_password(validated_data["password"])
        user.save()
        return user


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


class UserSerializer(serializers.ModelSerializer):
    comment_owner = CommentSerializer(many=True, read_only=True)
    liker = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'liker', 'comment_owner']


class UserSerializer(serializers.ModelSerializer):
    borrow_books=BorrowBookSerializer(many=True,read_only=True,source='borrow_user')

    class Meta:
        model=User
        fields=['id','username','email','borrow_books']
