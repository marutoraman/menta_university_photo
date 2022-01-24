from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from mysite.views import IndexView, LoginRequiredView
import debug_toolbar


urlpatterns = [
    path('', include('allauth.urls')),
    path('', IndexView.as_view(), name="index"),
    path('login_required', LoginRequiredView.as_view(), name="login_required"),
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('editlecture/', include('editlecture.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]