from . import views

from django.urls import path
urlpatterns = [
    
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path("logout", views.logout_view, name="logout"),
    path("login", views.user_login, name="login"),
    path("register", views.register, name="register"),
    path('product-detail', views.detail, name='product-detail'),
    path("anout", views.about, name="about"),
    path("faq", views.faq, name="faq"),
    path("contact", views.contact, name="contact"),
    # path("products", views.products, name="products"),
    path('auctions/', views.products, name='products'),
    path("create", views.create, name="create"),
    path('bid/<int:listing_id>/', views.bid, name='bid'),
    path('send_otp/', views.send_otp, name='send_otp'),
]
