from django.urls import path
from .views import ImageUploadView
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import async_to_sync


urlpatterns = [
    path('images/', csrf_exempt(async_to_sync(ImageUploadView.as_view())), name='upload'),
]
