
from django.contrib import admin
from django.urls import path
from api.views import home,index
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home),
    path('index/', index),
]
