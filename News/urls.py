# urls.py
from django.urls import path
from News.views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/<str:category>', views.blog, name='blog'),
    path('blog/', views.blog2, name='blog2'),
    path('article/<int:id>', views.article, name='article'),
    path('subscribe/', views.SubscribeView, name='subscribe'),
    path('contact/', views.ContactView, name='contact'),
]
