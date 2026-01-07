from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
    path('api/companies/', views.get_companies_api, name='companies_api'),
]
