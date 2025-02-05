from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path("uploadPost/",view=posts,name="uploadPost"),
]
