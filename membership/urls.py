from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<pk>/', views.movie, name='movie_view'),
    path('plans/', views.buy_subscription, name='buy_subs'),
    path('signup/', views.register, name='register'),
    path('signin/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('buy/<slug>/', views.payment_page, name='payment'),
    path('checkout/<slug>/', views.checkout, name='checkout'),
    path('confirm/', views.confirmCancel, name='cancel'),
    path('cancel/', views.cancel, name='cancel_mem'),
    path('profile/', views.userProfile, name='profile'),
]