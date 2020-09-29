from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('hobby_detail<int:item_id>', views.hobby_detail, name="hobby_detail"),
    path('portfolio_detail<int:item_id>', views.portfolio_detail, name="portfolio_detail"),
]