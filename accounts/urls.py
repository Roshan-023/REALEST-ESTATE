from django.urls import path
from .views import SignUpView, LoginView


urlpatterns = [
    path('login', LoginView.as_view(), name='token_obtain_pair'),
    path('signup', SignUpView.as_view())    
]
