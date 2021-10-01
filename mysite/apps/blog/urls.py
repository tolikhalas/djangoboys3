from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('<int:blog_id>/leave_comment',
         views.leave_comment, name='leave_comment'),
]
