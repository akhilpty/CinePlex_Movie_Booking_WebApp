
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
path('register-user',views.register_user,name="registeruser"),
path('login-user',views.login_user,name="loginruser"),
path('logout-user',views.logout_user,name="logoutuser"),
path('movie-list',views.usermovielist,name="usermovielist"),
path('movie-details/<int:id>',views.usermoviedetails,name="usermoviedetails"),
path("new-order/<int:id>", views.new_order),
path("callback", views.order_callback),
path("my-bookings", views.my_booking),
path('ticket-pdf/<int:angularid>', views.ticket_pdf, name='ticket_pdf'),
path('movie-add/<int:id>',views.booking_model_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
