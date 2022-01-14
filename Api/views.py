from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status, generics, mixins
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Book, Like, Comment
from .serializers import BookSerializer, LikeSerializer, CommentSerializer, ProfileViewSerializer, RegisterSerializer, UserSerializer
from .permission import IsCommentOwnerOrReadOnly

class BookViewset(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'like' or self.action == 'unlike':
            return [permissions.IsAuthenticated()]

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'like' or self.action == 'unlike':
            return LikeSerializer
        if self.action == 'comment':
            return CommentSerializer
        return super().get_serializer_class()

    @action(methods=['post'], detail=True)
    def like(self, request, pk=None):
        book = self.get_object()
        user = request.user
        Like.objects.get_or_create(book=book, user=user)
        return Response({'message': f"{book.name} liked by {user.username}"}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True)
    def unlike(self, request, pk=None):
        book = self.get_object()
        user = request.user
        qs = Like.objects.filter(book=book, user=user)
        if qs.count() != 0:
            qs.get().delete()
            return Response({'message': f"{book.name} unliked by {user.username}"}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True)
    def comment(self, request, pk=None):
        book = self.get_object()
        user = request.user
        Comment.objects.get_or_create(
            book=book, user=user, content=request.data['content'])
        return Response({'message': f"{book.name} comment created."}, status=status.HTTP_200_OK)


class LikeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class BorrowListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer


class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

