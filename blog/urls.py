from django.urls import path
from . import views

app_name= 'blog'

urlpatterns = [
    path('',views.ArticlesList.as_view(),name='home'), 
    path('<slug:blog_slug>/',views.ArticlesDetail.as_view(),name='details')
] 