from django.contrib import admin

from Api.models import Book, Comment,Like

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'ISBN','Author','name']
    search_fields=['Author']
 
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'book','user']
 
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'book','user','content']

from rest_framework_simplejwt import token_blacklist

class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True # or whatever logic you want

admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)