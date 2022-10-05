from django.contrib import admin
from django.urls import include,path
from django.urls import include, re_path
from django.conf import settings
from django.views.static import serve
from unity.views import Dashboard,Store


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',Dashboard,name="dashboard"),
    path('store/',Store,name="store"),
    path('api/',include('unity.urls',namespace='unity.api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
