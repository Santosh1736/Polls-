from django.urls import path
from . import views
from polls import views as polls_views
from django.contrib.auth import views as auth_views

app_name = 'polls'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/',views.ResultView.as_view(), name='result'),
    path('<int:question_id>/votes/',views.votes, name='votes'),
    path('Register/',polls_views.Register, name= "Register"),
    path('login/',auth_views.login,{'template_name': 'polls/login.html'}, name='login'),
    path('logout/',auth_views.logout,{'template_name': 'polls/logout.html'}, name='logout'),

]
