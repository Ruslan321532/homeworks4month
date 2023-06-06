from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('time/', views.now_time),
    path('goodbye/', views.goodby)
]
