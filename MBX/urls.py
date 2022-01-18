from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView)
from django.urls import path, include
from leads.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('news/', HomeView1.as_view(), name="news"),
    path('fikirlar/', FikirView.as_view(), name="Fikirlar"),
    path('creatf/', FikirCreatView.as_view(), name="Fikir-yaratish"),
    path('fikirlar/<int:pk>/', FikirDetailView.as_view(), name="Batafsil-fikirlar"),
    path('about/', AboutView.as_view(), name="Haqida"),
    path('<int:pk>/', HomePostView.as_view(), name="Single"),
    path('<int:pk>/pic', PicView.as_view(), name="Pic"),
    path('leads/', include('leads.urls', namespace="leads")),
    path('agents/', include('agents.urls', namespace="agents")),
    path('signup/', SigupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('password-reset-view/', PasswordResetView.as_view(), name="password_reset_view"),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-complate/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('password-tiklash/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('logout/', LogoutView.as_view(), name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)