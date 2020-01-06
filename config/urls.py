"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

from backend import views

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1'
    ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/list', views.member_list),
    path('member/create', views.member_form_create),
    path('member/<int:pk>/get', views.member_form_get),
    path('member/<int:pk>/update', views.member_form_update),
    path('member/<int:pk>/delete', views.member_delete),
    path('habit/list', views.habit_list),
    path('habit/create', views.habit_form_create),
    path('habit/<int:pk>/get', views.habit_form_get),
    path('habit/<int:pk>/update', views.habit_form_update),
    path('habit/<int:pk>/delete', views.habit_delete),
    path('type/options', views.type_option_list),
    path('type/create', views.type_create),

    url(r'^api-token-auth/', obtain_jwt_token),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
