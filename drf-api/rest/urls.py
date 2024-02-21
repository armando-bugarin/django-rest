from django.urls import path
from .views import RestList, RestDetail

urlpatterns = [
  path("", RestList.as_view(), name="rest_list"),
  path("<int:pk>/", RestDetail.as_view(), name="rest_detail"),
]