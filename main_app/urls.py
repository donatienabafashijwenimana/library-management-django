from django.urls import path
from.import  views
from .views import *

urlpatterns = [
    path('home/',views.dashboard_view,name='dashboard'),
    
    path('members/',memberview.as_view(),name='members'),
    path('searchmembers/',views.searchmember,name='searchmember'),
    path('members/add/',add_member.as_view(),name='addmember'),
    path('member/update/<pk>/',update_member.as_view(),name='updatemember'),
    path('member/delete/<pk>/',delete_member.as_view(),name='deletemember'),
    
    path('book/',bookview.as_view(),name='books'),
    path('searchbook/',views.searchbook,name='searchbook'),
    path('book/add/',add_book.as_view(),name='addbook'),
    path('book/update/<pk>/',updatebook.as_view(),name='updatebook'),
    path('book/delete/<pk>/',deletebook.as_view(),name='deletebook'),
    
    path('brower/',browerview.as_view(),name='brower'),
    path('brower/add/',add_brower.as_view(),name='addbrower'),
    path('brower/update/<pk>/',updatebrower.as_view(),name='updatebrower'),
    path('brower/return/<pk>/',return_book.as_view(),name='browerreturn'),
    path('brower/delete/<pk>/',delete_brower.as_view(),name='deletebrower'),
    
    path('brow_book/',views.browed_books,name='browedbooks'),
    
    path('logout/',views.logout,name='logout')
]
