from django.urls import path
from archemy.interfaces.views import *

urlpatterns = [
   path('all', ItemViews.items, name='items'),
   path('primes', ItemViews.prime_items),
   path('mirror', ItemViews.mirrors),
   path('from/', ItemViews.ItemfromUser.as_view()),
   path('user_from/', ItemViews.UserFromItem.as_view()),
   path('mirror/from/', ItemViews.MirrorfromUser.as_view()),
   path('new/', ItemViews.NewItem.as_view()),
   path('new/error', ExeptionViews.exception_parents),
   # path('from/aprove/', ItemViews.AprovefromUser.as_view()),
   # path('from/desaprove/', ItemViews.DesaprovefromUser.as_view()),
   path('aprove/', ItemViews.AproveItem.as_view()),
   path('desaprove/', ItemViews.DesaproveItem.as_view()),
   path('mirror/aprove/', ItemViews.AproveMirror.as_view()),
   path('mirror/desaprove/', ItemViews.DesaproveMirror.as_view()),

]