from django.urls import path
from .views import SignUpView
from .views import LoginView


urlpatterns = [
    path('token', LoginView.as_view(), name='token_obtain_pair'),
    path('signup', SignUpView.as_view())    
]
