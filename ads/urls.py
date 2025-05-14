from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.ad_list, name="ad_list"),
    path("create/", views.ad_create, name="ad_create"),
    path("<int:ad_id>/edit/", views.ad_update, name="ad_update"),
    path("<int:ad_id>/delete/", views.ad_delete, name="ad_delete"),
    path('<int:ad_id>/propose/', views.create_proposal, name='create_proposal'),
    path("proposals/", views.proposal_list, name="proposal_list"),
    path("proposals/<int:proposal_id>/update-status/",
         views.update_proposal_status, name="update_proposal_status"),


    path("login/", auth_views.LoginView.as_view(template_name="ads/login.html"),
         name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="ad_list"),
         name="logout"),
    path("register/", views.register, name="register"),

]
