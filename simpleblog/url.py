from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('',views.Home,name='home'),
     
    path('login/',views.User_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.Register,name='register'),
     path('create-blog/',views.CreateBlog,name='create-blog'),
    path('user-profile/<str:username>',views.User_profile,name='user-p'),

    path('details/<int:id>',views.Details,name='details'),

    path('update/<int:id>',views.Update_blog,name='update_blog'),

    path('delete/<int:id>',views.DeletBlog,name='delete_blog'),
    path('update-message/<int:id>',views.Updatemesags,name='update-message'),
    
    path('delte-message/<int:id>',views.delete_message,name='delete-message'),
     path('like/<int:id>',views.BlogLike,name='blog_like'),




]