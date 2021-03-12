from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.register),
    path('log_in', views.log_in),
    path('quotes', views.sucess),
    path('create_message', views.create_mess),
    path('logout', views.logout),
    path('delete/<int:mess_id>', views.delete_mess),
    path('user/<int:user_id>', views.profile),
    path('like/<int:user_id>', views.add_like),
    path('edit/<int:user_id>', views.edit),
    path('update/<int:user_id', views.update)
]