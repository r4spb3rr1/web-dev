from django.contrib import admin
from django.urls import path, include

from api.router import router, category_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(category_router.urls)),

]
