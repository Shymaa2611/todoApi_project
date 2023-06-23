from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('Tasks',views.TaskView,basename='Tasks')
urlpatterns=[
  
]
urlpatterns+=router.urls