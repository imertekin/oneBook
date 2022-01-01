from django.contrib import admin

from Api.models import Book,Borrow

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'ISBN','Author','is_avaible','name']
    search_fields=['borrow_book__user__username','Author']
 
@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ['id', 'Book','user']
 
