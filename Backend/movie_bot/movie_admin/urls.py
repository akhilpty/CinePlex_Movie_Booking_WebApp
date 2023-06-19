
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path("login-admin",views.admin_login,name="loginadmin"),
    path("logout-admin",views.admin_logout,name="logoutadmin"),
    path("add-movie",views.add_movie,name="addmovie"),
    path("edit-movie/<int:id>",views.edit_movie,name="editmovie"),
    path("delete-movie/<int:id>",views.delete_movie,name="deletemovie"),
    path("detail-movie/<int:id>",views.movie_details,name="moviedetails"),
    path('change-status', views.changestatus, name='changestatus'),
    path('search-movie', views.search_movie, name='searchmovie'),
    path('user-list', views.all_user, name='userlist'),
    path('user-status', views.user_status, name='userstatus'),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
