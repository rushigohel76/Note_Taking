from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup),
    
    path('signup/', views.signup, name='signup'),
    path('signup/submit/',views.submit_view, name='submit_view'),
    
    path('login/',views.login,name='login'),
    path('login/submit/',views.check_login, name='login_submit'),

    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),

    path('note_page/',views.note_page,name='note_page'),

]
