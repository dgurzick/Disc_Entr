from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Company
from .utils import load_companies_from_excel, import_companies_from_excel
import json


def landing_page(request):
    """Landing page with company selector"""
    # First time visiting? Import companies from Excel
    if Company.objects.count() == 0:
        import_companies_from_excel()
    
    companies = Company.objects.all().order_by('name')
    context = {
        'companies': companies,
    }
    return render(request, 'companies/landing.html', context)


def company_detail(request, company_id):
    """Detailed view for a specific company"""
    company = get_object_or_404(Company, id=company_id)
    steps = company.steps.all().order_by('step_number')
    
    # Group steps by theme
    steps_by_theme = {}
    for step in steps:
        theme = step.get_theme_display()
        if theme not in steps_by_theme:
            steps_by_theme[theme] = []
        steps_by_theme[theme].append(step)
    
    context = {
        'company': company,
        'steps_by_theme': steps_by_theme,
    }
    return render(request, 'companies/company_detail.html', context)


@require_http_methods(["GET"])
def get_companies_api(request):
    """API endpoint to get companies as JSON"""
    companies = Company.objects.all().values('id', 'name', 'year', 'sector')
    return JsonResponse({
        'companies': list(companies)
    })
