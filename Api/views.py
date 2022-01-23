from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status, generics, mixins
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Book, Like, Comment
from .serializers import BookSerializer, ChangePasswordSerializer, LikeSerializer, CommentSerializer, ProfileViewSerializer, RegisterSerializer, UserSerializer
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


class CommentView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet,):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwnerOrReadOnly]


class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProfileView(generics.ListAPIView, viewsets.ViewSet):
    serializer_class = ProfileViewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset
    
    def get_serializer_class(self):
        if self.action=="change_password":
            return ChangePasswordSerializer
        return super().get_serializer_class()

    @action(methods=['post'], detail=False)
    def change_password(self, request, pk=None):
        user=User.objects.get(username=request.user)
        serializer=ChangePasswordSerializer(data=request.data)
        # print(user.check_password('test'))
        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                 return Response({"message": "Wrong password."}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"Message":"Password changed successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)