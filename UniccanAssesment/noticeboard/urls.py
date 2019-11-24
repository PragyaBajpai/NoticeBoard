from django.urls import path
from .views import index,NoticeBoardCreateView,NoticeBoardDeleteView,NoticeBoardListView,NoticeBoardDetailView,NoticeBoardUpdateView

urlpatterns = [
    path('', index , name="index"),
    path('noticeboard-createview/', NoticeBoardCreateView.as_view() , name="create-noticeboard"),
    path('noticeboard-deleteview/<int:pk>/', NoticeBoardDeleteView.as_view() , name="delete-noticeboard"),
    path('noticeboard-listview/', NoticeBoardListView.as_view() , name="list-noticeboard"),
    path('noticeboard-detailview/<int:pk>/', NoticeBoardDetailView.as_view() , name="detail-noticeboard"),
    path('noticeboard-updateview/<int:pk>/', NoticeBoardUpdateView.as_view() , name="update-noticeboard"),
]