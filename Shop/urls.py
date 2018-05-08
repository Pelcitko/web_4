# -*- coding: utf-8 -*-
"""
URL settings for RuzePelcovi.cz
@author: LP
"""

from django.urls import path
from . import views

# app_name = 'Shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('rose_list/', views.rose_list),
    path('list/', views.RoseList.as_view(), name='rose_list'),
    path('<pk>/', views.RoseDetail.as_view(), name='rose_detail'),
    # path('accounts/profile(|/saved)/', views.profile),
]
