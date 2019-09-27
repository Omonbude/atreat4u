<<<<<<< HEAD
from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

=======
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from . import views
  
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c


app_name = "account"
urlpatterns = [
<<<<<<< HEAD
	#url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
	# url('password_reset/$', include('django.contrib.auth.urls')),
#  	url(r'^register/$', views.register, name='register'),
#  	url(r'^login/$',views.login_page, name='login'),
#  	url(r'^logout/$',views.logout_page, name='logout'),
# 	path('reset_password/', views.reset_password, name='test'),
# 	path('reset_password_confirm/', views.reset_password_confirm, name='reset_password_confirm'),
	path('change_password/', views.change_password, name='change_password'),
	path('change_password_confirm/', views.change_password_confirm, name='change_password_confirm'),
	path('<slug:pk>', views.change_password_code, name='change_password_code'),
	path('change_password_success/', views.change_password_success, name='change_password_success'),
	path('edit_profile/', views.edit_profile, name='edit_profile'),
	path('profile/', views.profile, name='profile'),
	path('login/', views.login_page, name='login'),
	path('logout/', views.logout_page, name='logout'),
	path('logged_out/', views.logged_out, name='logged_out'),
	path('register/', views.register, name='register'),
	path('register_success/', views.registration_success, name='registration_success'),
    # path('register', views.register, name='register'),
    # path('login', views.login_page, name='login'),
    # path('logout', views.logout_page, name='logout'),




]
=======
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
	# url('password_reset/$', include('django.contrib.auth.urls')),
 	url(r'^register/$', views.register, name='register'),
 	url(r'^login/$',views.login_page, name='login'),
 	url(r'^logout/$',views.logout_page, name='logout'),
 	# url(r'^logout/$', auth_views.logout, name='logout'),



] 
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
