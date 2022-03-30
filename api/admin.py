from django.contrib import admin

from .models import Comment, Post


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'created_date')
    list_filter = ('created_date',)
    readonly_fields = ('amount_upvotes',)
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)


