from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path
from django.views.static import serve

import courses
from courses.views import CourseListView

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('course/', include('courses.urls', namespace='course')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('students/', include('students.urls', namespace='students')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('admin/', admin.site.urls),
    path('', CourseListView.as_view(), name="course_list"),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)
