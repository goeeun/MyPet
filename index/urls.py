from django.urls import path
from django.conf.urls import include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index/', views.index, name= 'index'),
    path('', views.index, name= 'index'),
    path('favorites/', views.favorites, name= 'favorites'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)