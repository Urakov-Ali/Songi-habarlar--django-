from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns =[
    path('',IndexView.as_view(), name='index'),
    path('page/<int:page_id>', page_view, name='page_view'),
    path('category/<int:cat_id>', cat_view, name='cat_view')
    ] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
