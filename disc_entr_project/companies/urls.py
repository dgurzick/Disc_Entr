from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('companies/', views.companies_list, name='companies_list'),
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
    path('api/companies/', views.get_companies_api, name='companies_api'),
]
