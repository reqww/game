from django.urls import path 
from accounts import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
	path('login/', views.log_in, name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('register/', views.register, name='register'), 
	path('edit/', views.edit, name="edit"), 
	path('password-change/',views.PasswordChangeView.as_view(),name='password_change'),
	path('pwd-reset/',
		auth_views.PasswordResetView.as_view(),
		name='password_reset'),
	path('pwd-reset/done/',
		auth_views.PasswordResetDoneView.as_view(),
		name='password_reset_done'),
	path('pwd-reset/<uidb64>/<token>/',
		auth_views.PasswordResetConfirmView.as_view(),
		name='password_reset_confirm'),
	path('pwd-reset/complete/',
		auth_views.PasswordResetCompleteView.as_view(),
		name='password_reset_complete'),
]