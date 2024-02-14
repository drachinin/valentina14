from django.urls import path, include


urlpatterns = [
    path('', include('main.urls')),
    path('yes.html', include('main.urls'))
]
