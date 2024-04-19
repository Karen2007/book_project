from django.contrib import admin
from django.urls import path
from books.views import home, register, login, forum
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('forum/', forum, name='forum'),
    path('login/', login, name='login'),
    path('register/', register, name='register')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
