from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="discussion"),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', views.DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', views.CategoryView.as_view(), name='category'),    
    # path('category_list/', views.CategoryListView, name='category_list'),
    path('article/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('discussion/comment/edit/<int:pk>/', views.UpdateCommentView.as_view(), name='update_comment'),
    path('discussion/comment/<int:pk>/delete', views.DeleteCommentView.as_view(), name='delete_comment'),
]
