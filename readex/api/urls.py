from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view),
    path('signup/', views.signup),
    path('logout/', views.logout_view),
    path('checklogin/', views.check_user_login),



    path('profiles/', views.profile_list, name='profile-list'),
    path('profiles/<int:pk>/', views.profile_detail, name='profile-detail'),
    path('communities/', views.community_list, name='community-list'),
    path('communities/<int:pk>/', views.community_detail, name='community-detail'),
    path('memberships/', views.membership_list, name='membership-list'),
    path('memberships/<int:pk>/', views.membership_detail, name='membership-detail'),
    path('posts/', views.post_list, name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('likes/', views.like_list, name='like-list'),
    path('likes/<int:pk>/', views.like_detail, name='like-detail'),
    path('comments/', views.comment_list, name='comment-list'),
    path('comments/<int:pk>/', views.comment_detail, name='comment-detail'),


]