"""
URL configuration for delightscafe project.

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
from django.urls import path
from delightsapp import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.menu_view, name="home"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('ingredients/', views.IngredientList.as_view(), name="ingredients"),
    path('purchases/', views.PurchaseList.as_view(), name="purchases"),
    path('menu/', views.MenuItemList.as_view(), name="menu"),
    path('balance/', views.show_balance, name="balance"),
    path('ingredients/create', views.IngredientCreate.as_view(), name="ingredientcreate"),
    path('ingredients/<pk>/update', views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path('ingredients/<pk>/delete', views.IngredientDelete.as_view(), name="ingredientdelete"),
    path('menu/create', views.MenuItemCreate.as_view(), name="menucreate"),
    path('menu/<pk>/update', views.MenuItemUpdate.as_view(), name="menuupdate"),
    path('menu/<pk>/delete', views.MenuItemDelete.as_view(), name="menudelete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
