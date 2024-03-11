from django.urls import path

from user_management.views import LOGIN, doLogin,hod_home, user_base,do_logout,driver_details



from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user_base/',user_base,name='user_base'),
    path('login/', LOGIN, name='login'),
    path('do_logout/',do_logout, name='do_logout'),
    path('doLogin/', doLogin, name='doLogin'),
    path('hod_home/', hod_home, name='hod_home'),
    path('driver_details/',driver_details, name='driver_details')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

