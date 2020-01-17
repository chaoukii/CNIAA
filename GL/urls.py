from django.contrib import admin
from django.urls import path
from workshop import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('data/', views.data, name='data'),
    path('program/', views.program, name='program'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('login/', auth_views.LoginView.as_view(),
        {'template_name': 'login.html'},
        name='login'),
    path('signout/', auth_views.LogoutView.as_view(),
        {'next_page': '/'},
        name='logout'),
    path('login/account/', views.account_home, name='account_home'),
    path('login/account/submit', views.submit, name='submit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
