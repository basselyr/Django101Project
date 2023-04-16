from django.urls import path
from .views import HomeView, PostDetailView, AddPostView

app_name = 'feed'

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/', AddPostView.as_view(), name="post")
]