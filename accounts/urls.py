from django.urls import path
from .views import SignUpView, LoginView
from .views import RealtorListView, RealtorView, TopSellerView


urlpatterns = [
    path('login', LoginView.as_view(), name='token_obtain_pair'),
    path('signup', SignUpView.as_view()),
    path('user-list', RealtorListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', RealtorView.as_view())   
]

