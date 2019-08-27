from django.urls import include,path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Quote',views.QuoteView)
router.register('Item',views.ItemView)

#
urlpatterns = [
    path('',include(router.urls)),
    path('',include(router.urls)),

]