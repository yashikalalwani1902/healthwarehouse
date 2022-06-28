from django.urls import path
from django.views.generic.base import RedirectView
from django.urls.conf import include
from app import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers



router = routers.DefaultRouter() 
router.register(r'medicine', views.MedicineViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'review', views.ReviewViewSet)


urlpatterns = [
    # static page urls here
    path('index/',views.IndexView.as_view()),
    path('about/',views.AboutView.as_view()),
    
    path('contact/',views.ContactView.as_view()),
    path('contact/send',views.contactform),
    
    #dynamic pages urls here
    path('store/',views.StoreView.as_view(),name='store'),
    path('store/medicine/view/<int:id>',views.MedicineDetailView.as_view(),name='med_detail'),
    path('store/medicine/cart/<int:id>',views.MedicineCartView.as_view(),name='med_cart'),
    path('store/medicine/order/',views.OrderMedicine,name='med_order'),
    
    path('orders/',views.OrdersView.as_view(),name='orders'),
    path('orders/review/<int:id>',views.OrdersReviewView.as_view(),name='order_review'),
    path('orders/review/done',views.ReviewDone,name='order_rating_done'),
     
    path('profile/edit/<int:pk>',views.ProfileUpdateView.as_view()),
     
    path(r'api/', include(router.urls)),
    path(r'api-token-auth/', obtain_jwt_token),
    
    path('',RedirectView.as_view(url='index/'))
]
