from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update-item/', views.update_item, name='update-item'),
    path('process-order/', views.process_order, name='process-order'),
]
