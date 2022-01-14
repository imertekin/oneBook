from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status, generics, mixins
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Book, Like, Comment
from .serializers import BookSerializer, LikeSerializer, CommentSerializer, ProfileViewSerializer, RegisterSerializer, UserSerializer

class BookViewset(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes =[permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action=='take'or self.action=='untake':
           return [permissions.IsAuthenticated()]

        return super().get_permissions()

    @action(methods=['post'],detail=True)
    def take(self,request,pk=None):
        book=self.get_object()
        user=request.user
        if book.is_avaible==False:
            return Response({'message':"This book is not on the shelf"},status=status.HTTP_404_NOT_FOUND)
        
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




class BorrowListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer


class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

