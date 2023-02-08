from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<slug:pk>/', views.room, name="room"),
    path('profile/<slug:pk>/', views.userProfile, name='user-profile'),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<slug:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<slug:pk>', views.deleteRoom, name="delete-room"),
    path('delete-message/<slug:pk>', views.deleteMessage, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
]