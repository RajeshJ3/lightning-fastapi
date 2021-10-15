from api.helpers import path
from accounts import views

urlpatterns = [
    path('/', views.index, 'GET')
]
