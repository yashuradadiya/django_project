"""
URL configuration for Ultras project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from UltrasApp.views import *
from admin_ultras.views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('blog_masonny/', blog_masonny),
    path('blog_sidebar/', blog_sidebar),
    path('blog/', blog),
    path('cart/', cart),
    path('myadmin/view_cart/', view_cart),
    path('add_cart/<int:product_id>', add_cart),
    path('cancle_cart/<int:cart_id>', cancle_cart),
    path('cancle_wishlist/<int:wishlist_id>', cancle_wishlist),
    path('buy/<int:product_id>', buy),
    path('add_wishlist/<int:product_id>', add_wishlist),
    path('checkout/', checkout),
    path('coming_soon/', coming_soon),
    path('contact/', contact),
    path('error/', error),
    path('faqs/', faqs),
    path('login/', login),
    path('profiles/', profiles),
    path('shop/', shop),
    path('shop_grid/', shop_grid),
    path('shop_list/', shop_list),
    path('shop_slider/', shop_slider),
    path('single_post/', single_post),
    path('single_product/<int:product_id>', single_product),
    path('thank_you/', thank_you),
    path('wishlist/', wishlist),
    path('index/', index), 
    path('myadmin/', a_index),
    path('myadmin/index/', a_index),
    path('myadmin/register/', register),
    path('myadmin/home/', home),
    path('myadmin/profile/', profile),
    path('myadmin/setting/', setting),
    # slider
    path('myadmin/view_slider/', view_slider),
    path('myadmin/add_slider/', add_slider),
    path('myadmin/edit-slider/<int:edit_id>', edit_slider),
    path('myadmin/delete-slider/<int:del_id>', delete_slider),
    # category
    path('myadmin/view_category/', view_category),
    path('myadmin/add_category/', add_category),
    path('myadmin/edit-category/<int:edit_id>', edit_category),
    path('myadmin/delete-category/<int:del_id>', delete_category),
    # tag
    path('myadmin/view_tag/', view_tag),
    path('myadmin/add_tag/', add_tag),
    path('myadmin/edit-tag/<int:edit_id>', edit_tag),
    path('myadmin/delete-tag/<int:del_id>', delete_tag),
    # brand
    path('myadmin/view_brand/', view_brand),
    path('myadmin/add_brand/', add_brand),
    path('myadmin/edit-brand/<int:edit_id>', edit_brand),
    path('myadmin/delete-brand/<int:del_id>', delete_brand),
    # product
    path('myadmin/view_product/', view_product),
    path('myadmin/add_product/', add_product),
    path('myadmin/edit-product/<int:edit_id>', edit_product),
    path('myadmin/delete-product/<int:del_id>', delete_product),
    # view user
    path('myadmin/view_user/', view_user),
    path('myadmin/edit-user/<int:edit_id>/<str:status>/', edit_user, name='edit_user'),
    # logout
    path('logout/', logout),
    path('logouts/', logouts),
    path('myadmin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
