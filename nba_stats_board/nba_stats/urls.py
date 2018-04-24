# coding: utf-8

from django.urls import path

from . import apiviews

urlpatterns = [
    path('teams/', apiviews.TeamListView.as_view(), name='api_team_list'),
    path('teams/<int:pk>', apiviews.TeamDetailView.as_view(), name='api_team_detail'),
    path('teams/create/', apiviews.TeamCreateView.as_view(), name='api_team_create')
]
