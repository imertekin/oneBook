from django.contrib.auth.models import  User
from rest_framework import  viewsets,permissions,status
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Book, Borrow
from .serializers import BookSerializer, BorrowSerializer, UserSerializer


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
        
        book.is_avaible=False
        book.save()
        Borrow.objects.get_or_create(Book=book,user=user)
        return Response({'message':f"Book taken by {user.username}"},status=status.HTTP_200_OK)
    
    @action(methods=['post'],detail=True)
    def untake(self,request,pk=None):
        book=self.get_object()
        user=request.user
        qs=Borrow.objects.filter(Book=book,user=user)
        if len(qs)==0:
            return Response({'message':"This book has not already been taken by you."},status=status.HTTP_404_NOT_FOUND)
        
        qs.get().delete()
        book.is_avaible=True
        book.save()
        return Response({'message':"The book has been delivered."},status=status.HTTP_200_OK)




class BorrowListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer


class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

