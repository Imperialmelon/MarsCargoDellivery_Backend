"""
URL configuration for lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from app import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Mars cargo delivery API",
      default_version='v1',
      description="API for Mars cargo delivery",
      contact=openapi.Contact(email="spacey@google.com"),
      license=openapi.License(name="SAPCE Y License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('cargoes', views.Get_CargoList, name='cargo_list'), #+
    path('shippings', views.get_shippings_list, name='shipping_list'), #+
    path('shipping/<int:pk>/change', views.change_shipping, name='shipping_change'), #+
    path('shipping/<int:pk>', views.get_shipping, name='shipping'), #+
    path('shipping/<int:pk>/form', views.form_shipping, name='form_shipping'), #+
    path('cargo/add', views.add_Cargo, name='cargo_add'), #+
    path('cargoes/<int:pk>/change', views.Change_Cargo, name='cargo_change'), #+
    path('cargo/<int:pk>', views.Get_Cargo, name='cargo'), #+
    path('cargo/<int:pk>/add_to_shipping', views.CreateShipping, name='form_cart'), #+
    path('cargo/<int:pk>/add_image', views.load_image_to_minio, name='add_image'), #+
    path('cargoes/<int:pk>/delete', views.Delete_Cargo, name='cargo_removal'), #+
    path('shipping/<int:pk>/delete', views.delete_shipping, name='shipping_removal'), #+
    path('shipping/<int:pk>/resolve', views.resolve_Shipping, name='resolve_shipping'), #+
    path('shipping_cargo/<int:ck>/<int:sk>/change', views.change_shipping_cargo, name='change_shipping_cargo'), #+
    path('shipping_cargo/<int:ck>/<int:sk>/delete', views.delete_cargo_from_shipping, name='delete_shipping_cargo'), #+
    path('user/create', views.create_user, name='user_create'), #+
    path('user/logout/', views.logout_user, name='user_logout'), #+
     path('user/login/', views.login_user, name='user_login'), #+
     path('user/update', views.update_user, name='user_update'), #+
]