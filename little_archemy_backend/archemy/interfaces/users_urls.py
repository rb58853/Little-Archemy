from django.urls import path
from archemy.interfaces.views import *

urlpatterns = [
   path('all', UserViews.users, name='users'),
   path('credits/', UserViews.CreditsFromUser.as_view()),
   path('data/', UserViews.DataFromUser.as_view()),
   path('set_admin/', UserViews.SetAdmin.as_view()),
   path('new/', UserViews.NewUser.as_view()),
]