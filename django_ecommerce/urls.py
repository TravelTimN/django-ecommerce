from django.urls import include, path
from django.contrib import admin
from accounts import urls as urls_accounts
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from products import urls as urls_products
from search import urls as urls_search
from products.views import all_products
from django.views.static import serve
from .settings import MEDIA_ROOT


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", all_products, name="index"),
    path("accounts/", include(urls_accounts)),
    path("cart/", include(urls_cart)),
    path("checkout/", include(urls_checkout)),
    path("products/", include(urls_products)),
    path("search/", include(urls_search)),
    path("media/<path:path>", serve, {"document_root": MEDIA_ROOT}),
]
