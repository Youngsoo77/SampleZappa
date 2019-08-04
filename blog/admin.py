from django.contrib import admin

from blog.models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at', 'is_published']
    list_display_links = ['id', 'name', ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_category', 'title', 'get_author_name', 'created_at', 'updated_at', 'is_published']
    list_display_links = ['id', 'title', ]

    def get_author_name(self, obj):
        return obj.author.username if obj.author else None

    def get_category(self, obj):
        return obj.category.name if obj.category else None

    get_author_name.admin_order_field = 'author'
    get_author_name.short_description = 'Author Name'
    get_category.admin_order_field = 'category'
    get_category.short_description = 'Category'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_body'] + [field.name for field in Comment._meta.get_fields() if
                                           field.name not in ['id', 'body', 'post']]
    list_display_links = ['short_body']
