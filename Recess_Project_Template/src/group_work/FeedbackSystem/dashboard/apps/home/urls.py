# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from FeedbackSystem.dashboard.apps.home import views

# app_name = 'home'

urlpatterns = [

    # The home page
    path('dashboard', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
