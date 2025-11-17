from django.urls import path, include
from accounts.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)