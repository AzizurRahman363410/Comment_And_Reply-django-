from django.contrib import admin
from . models import Post,Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','message','reply_id','post_id',)



admin.site.register(Post)
admin.site.register(Comment,CommentAdmin)