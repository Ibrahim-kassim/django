from django.urls import path
from . import views


urlpatterns = [
    # 3 parameters
    path("", views.home,name="home"),
    path("room/<str:pk>/",views.room,name="room"),
    path("create-room/" , views.createRoom , name="create-room"),
    path("update-room/<str:pk>" , views.updateRoom,name="update-room"),
    path("delete-room/<str:pk>" , views.deleteRoom,name="delete-room"),


    # path("cars",views.cars_view,name="cars"),
    # path("cartype/<str:pk>",views.cartype,name="cartype")

]