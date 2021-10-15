from api.helpers import path
from accounts.urls import urlpatterns as accounts_urls
from accounts import views

urlpatterns = [
    path('/contact', views.contact, 'GET'),
    path('/', accounts_urls),
]
