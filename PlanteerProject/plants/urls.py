from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path("all/", views.plants_all, name="plants_all"),
    path("detail//<plant_id>/", views.detail_page, name="detail_page"),
    path("add/", views.add_new_page, name="add_new_page"),
    path("update/<plant_id>/", views.update_page, name="update_page"),
    path('delete/<plant_id>/', views.plant_delete_view, name='plant_delete'),

    path("search/", views.search_page, name="search_page"),

]