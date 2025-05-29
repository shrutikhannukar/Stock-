from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base,name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # admin
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/update/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),

    # user
    path('profile/', views.user_profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),

    # # 2021453
    path('stocks/', views.stock_data_list, name='stock_data_list'),

    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/add/', views.portfolio_add, name='portfolio_add'),
    path('portfolio/edit/<int:pk>/', views.portfolio_edit, name='portfolio_edit'),
    path('portfolio/delete/<int:pk>/', views.portfolio_delete, name='portfolio_delete'),

    path('generate-predictions/', views.generate_predictions, name='generate_predictions'),

    path('graph/', views.graph,name='graph'),
    path('stocks/<int:pk>/', views.stock_detail, name='stock_detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
