from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PhotoViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('deletephotos/<int:photo_id>/', PhotoViewSet.delete, name='delete_photo'),
    path('settages/<int:photo_id>/<str:tages>/', PhotoViewSet.setTage, name='set_tage'),

]
