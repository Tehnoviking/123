from django.urls import re_path,path
from .views import CategoriesListView,DiscountListView,ProducerListView,PromocodeListView,ProductItemListView,CategoryProductsView,ProducerProductView,DiscountProductsView,RegistrationView,ActivateAccountView,LoginView,BasketView,CreateOrderView,SingleProductItemView,GetStatisticView

urlpatterns = [
    re_path(r'^categories-all',CategoriesListView.as_view(),name='categories-all'),
    re_path(r'^promocode-all',PromocodeListView.as_view()),
    re_path(r'^producer-all',ProducerListView.as_view()),
    re_path(r'^productitem-all',ProductItemListView.as_view()),
    re_path(r'^discount-all',DiscountListView.as_view()),

    path('category/<int:cat_id>/',CategoryProductsView.as_view()),
    path('producer/<int:producer_id>/',ProducerProductView.as_view()),
    path('discount/<int:discount_id>/',DiscountProductsView.as_view()),
    path('product/<int:product_id>/',SingleProductItemView.as_view()),

    re_path(r'^register/',RegistrationView.as_view()),
    re_path(r'^login/',LoginView.as_view()),
    re_path(r'^basket/',BasketView.as_view()),
    re_path(r'^create-order/',CreateOrderView.as_view()),
    re_path(r'^get-statistic/',GetStatisticView.as_view()),


    path('activate/<slug:uidb64>/<slug:token>/', ActivateAccountView.as_view(), name='activate')


]

