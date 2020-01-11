from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name="home"),
    path('new/project/',views.post_project_view,name="post-project"),
    path('review/project/<int:id>',views.post_review_view, name='post-review'),
    path('review/project/post/<int:id>',views.review_post,name="review_submit"),
    path('review/project/rate/post/<int:id>',views.post_rate_view, name='post-rate'),
    
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)