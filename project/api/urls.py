from django.urls import path
from rest_framework import routers

from project.api import views

urlpatterns = [
    # path('', views.ProjectAPIView.as_view(), name='project')

]

router = routers.SimpleRouter()
router.register(r'', views.ProjectViewSet)
urlpatterns += router.urls
