from django.urls import path, re_path

from .views import PostListView, PostDetailView 

urlpatterns = [
	re_path(r'^$', PostListView.as_view(), name='list'),
    re_path(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), 
                                              

]