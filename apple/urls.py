from django.urls import include, path
from django.urls import re_path as url
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('bikes/',views.bikespage,name='bikes'),
    path('book/',views.book, name='book'),
    url(r'^status/(?P<id>\d{1,3} )/$',views.book_process),
    url(r'^return_status/(?P<id>\d{1,3})/(?P<id1>\d{1,3})/$',views.return_process),
    path('cart/',views.cart)
]
