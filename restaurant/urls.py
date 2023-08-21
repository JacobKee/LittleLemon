from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),

    path('api/bookings/', views.BookingView.as_view()),
    path('api/menu-items/', views.MenuItemsView.as_view()),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),

]
