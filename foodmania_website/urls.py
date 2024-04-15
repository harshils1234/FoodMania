from django.urls import path
from foodmania_website.views import HomePageView, OrderListView, OrderDetailView, \
    CheckoutView, AddToCartView, CartView, IncreaseItemQuantityView, DecreaseItemQuantityView, \
    RemoveItemFromCartView, AdminDashboardView, order_payment, callback, OrderDeliveredStatusView, \
    OrderRefundedStatusView, NewsLetterView

app_name = 'foodmania_website'

urlpatterns = [


    path('', HomePageView.as_view(), name='website'),
    path('dashboard/', AdminDashboardView.as_view(), name='dashboard'),

    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('increase-quantity/<int:pk>/', IncreaseItemQuantityView.as_view(), name='increase_quantity'),
    path('decrease-quantity/<int:pk>/', DecreaseItemQuantityView.as_view(), name='decrease_quantity'),
    path('remove-from-cart/<int:pk>/', RemoveItemFromCartView.as_view(), name='remove_from_cart'),

    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/', order_payment, name='payment'),
    path('callback/', callback, name='callback'),
    path('order/list/', OrderListView.as_view(), name='order_list'),
    path('order/status/delivered/<int:pk>/', OrderDeliveredStatusView.as_view(), name='delivered_status'),
    path('order/status/refunded/<int:pk>/', OrderRefundedStatusView.as_view(), name='refunded_status'),
    path('order/detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('newsletter/', NewsLetterView.as_view(), name='newsletter')


]

from django.contrib.auth.views import LogoutView
