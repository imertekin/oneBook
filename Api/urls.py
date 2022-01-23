from django.urls import include,path

from rest_framework.routers import DefaultRouter

from .views import BookViewset,LikeViewSet, UserViewset,ProfileView,CommentView,BookListViewSet

router = DefaultRouter()

router.register(r'books', BookViewset, basename='books')
router.register(r'like',LikeViewSet,basename='like')
router.register(r'booklist',BookListViewSet,basename='booklist')
router.register(r'comment',CommentView,basename='comment')
router.register(r'users',UserViewset,basename='users')
router.register(r'profile',ProfileView,basename='profile')
urlpatterns = [
    path('',include(router.urls)),
    
]


