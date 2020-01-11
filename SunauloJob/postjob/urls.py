from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', post_job),
    path('post/save', save_posted_job),
    path('data/delete/<int:ID>',delete_post),
    path('search',search_data)
]
