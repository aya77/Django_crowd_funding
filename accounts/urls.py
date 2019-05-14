from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view

app_name = 'accounts'

urlpatterns = [
  path('login/', views.user_login, name='login'),
  path('logout/', auth_view.LogoutView.as_view(), name='logout'),
  path('signup/', views.Signup.as_view(), name='signup'),
  path('activate/<str:uid>/<str:token>', views.Activate.as_view(), name='activate'),
  url(r'^edit-profile/(?P<pk>\d+)$', views.Edit_profile.as_view(), name='edit_profile'),
]
