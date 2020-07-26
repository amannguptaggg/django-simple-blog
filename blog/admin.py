from django.contrib import admin
from .models import Articles,Author,Comment


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_slug','status','updated_on','created_on')
    list_filter = ('status',)
    search_fields = ['blog_title','content']
    prepopulated_fields = {'blog_slug':('blog_title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','post','created_on','active')
    list_filter = ('active','created_on')
    search_fields = ('name','email','body')
    actions = ['approve_comments']

    def approve_comments(self, request, quesryset):
        quesryset.update(active=true)


admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Author)
admin.site.register(Comment,CommentAdmin)