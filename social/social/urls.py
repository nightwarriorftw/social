from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts.views import (
    home,
    auth_login,
    auth_register,
    auth_logout,
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', auth_login, name="login"),
    path('register/', auth_register, name="register"),
    path('logout/', auth_logout, name='logout'),
    path('feed/', include("accounts.urls", namespace='feed' )),
    path('donation/', include("donation.urls", namespace="donation")),
]

if settings.DEBUG == True:
    urlpatterns = urlpatterns + static(
            settings.STATIC_URL, document_root=settings.STATIC_ROOT
        )
    urlpatterns = urlpatterns + static(
                settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
            )
