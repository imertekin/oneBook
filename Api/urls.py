from django.urls import include,path

from rest_framework.routers import DefaultRouter

from .views import BookViewset,BorrowListCreateView, UserViewset

router = DefaultRouter()
router.register(r'books', BookViewset, basename='books')
router.register(r'borrows',BorrowListCreateView,basename='borrows')
router.register(r'users',UserViewset,basename='users')
urlpatterns = [
    path('',include(router.urls))
]


