from django.contrib import admin
from django.urls import path
from .import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('view-orders/', views.orders, name='orders'),
    path('view-orders-json/', views.jsondata),
    path('view-order/<str:order_number>', views.view_order, name='view-order'),
    path('order/', views.order, name='make_order'),
    path('change-order/<str:order_number>', views.change_order, name='change-order'),
    path('cancel-order/<str:order_number>', views.cancel_order, name='cancel-order'),
    path('post-ordering/<str:order_number>', views.post_ordering, name='post-ordering'),
    path('work/', views.work_login, name="work_login"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('registrer/', views.registrer, name="registrer"),
    path('404/', views.not_found, name="not_found"),

    path('react/',TemplateView.as_view(template_name="react.html"), name="orders")

]