from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    # Redirect root URL to the API landing
    path('', RedirectView.as_view(url='/api/', permanent=False)),
]
