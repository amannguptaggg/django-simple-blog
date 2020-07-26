from django.db import models


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Articles(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_slug = models.SlugField(max_length=250,null=True, blank=True)
    author_name = models.ForeignKey('Author',on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS,default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.blog_title


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField()

    def __str__(self):
        return self.author_name


class Comment(models.Model):
    post = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.name)
 