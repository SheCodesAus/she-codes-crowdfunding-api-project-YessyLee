from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"),#always include name on urls
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project-detail"),
    path('pledges/', views.PledgeList.as_view(), name="pledge-list")
]

urlpatterns = format_suffix_patterns(urlpatterns) #function that take urls whether it take json or other file, rpobably will be deleted
