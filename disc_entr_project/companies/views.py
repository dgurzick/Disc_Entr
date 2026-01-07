from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Company
from .utils import load_companies_from_excel, import_companies_from_excel
import json


def home_page(request):
    """Home page focused on Nesterly case study"""
    # Nesterly company data from research
    nesterly_data = {
        'name': 'Nesterly',
        'tagline': 'Intergenerational homesharing platform',
        'founded': '2016-2017',
        'founders': [
            {'name': 'Noelle Marcus', 'role': 'CEO', 'background': 'NYC Economic Development Corporation'},
            {'name': 'Rachel Goor', 'role': 'Co-founder (departed ~2018)', 'background': 'San Francisco housing programs'},
            {'name': 'Shaun Klopfenstein', 'role': 'CTO & Co-founder (joined Oct 2018)', 'background': 'Crowd Factory'},
        ],
        'origin': 'MIT Housing, Community, and Economic Development master\'s program',
        'inspiration': 'Airbnb\'s response to Hurricane Sandy in 2012',
        'team_size': '7-10 employees',
        'funding': {
            'total': '$15,000 (formal)',
            'grants': [
                'MIT IDEAS Global Challenge: $7,500',
                'MIT Sandbox: $5,000',
            ],
            'accelerators': ['MassChallenge', 'Grand Central Tech'], 
            'investors': ['Access Ventures', 'Impact Assets', 'Blue Ridge Labs', 'GC Venture Fellows'],
        },
        'markets': [
            {'name': 'Greater Boston', 'since': '2017', 'status': 'Active'},
            {'name': 'Central Ohio/Columbus', 'since': '2019', 'status': 'Active'},
            {'name': 'Louisville', 'since': None, 'status': 'Active'},
            {'name': 'Greater Pittsburgh', 'since': None, 'status': 'Active'},
            {'name': 'Town of Poughkeepsie', 'since': None, 'status': 'Active'},
            {'name': 'Maine (Statewide)', 'since': 'April 2024', 'status': 'Active'},
            {'name': 'Nashville-Davidson County', 'since': 'Summer 2025', 'status': 'Launching'},
            {'name': 'Bellingham-Whatcom County, WA', 'since': None, 'status': 'Coming Soon'},
        ],
        'business_model': {
            'booking_fee': '$95-195 (one-time)',
            'service_fee': '2.5% monthly (both host and guest)',
            'avg_rent': '$300-$900/month',
            'host_earnings': '$6,600 annually (average)',
            'min_stay': '30 days',
        },
        'key_metrics': {
            'columbus': {
                'housing_days': '2,000+',
                'avg_stay': '180 days',
                'avg_rent': '$500/month',
                'task_exchange_rate': '33%',
            },
            'boston': {
                'active_listings': '22 (as of Feb 2024)',
            },
        },
        'maine_contract': {
            'value': '$200,000',
            'significance': 'First statewide homesharing contract nationally',
            'partners': ['MaineHousing', 'AARP Maine', 'Maine Council on Aging', "Governor's Cabinet on Aging"],
            'legislation': 'LD 709 (July 2023)',
        },
        'safety_features': [
            'Comprehensive background checks via Checkr',
            'National criminal search',
            'Sex offender registry check',
            'Global watchlist screening',
            'Social Security verification',
            'Two reference requirements',
            'Licensed social workers for monthly check-ins',
        ],
        'task_exchange': {
            'discount': '$100-150/month',
            'hours': '2-3 hours weekly',
            'tasks': ['Grocery pickup', 'Technology help', 'Dog walking', 'Light chores'],
        },
        'market_opportunity': {
            'homes_available': '21 million U.S. homes with older residents and spare bedrooms',
            'senior_living_market_2024': '$907.59 billion',
            'senior_living_market_2033': '$1.33 trillion',
            'aging_in_place_market': '$151 billion annually',
            'growth_rate': '13% CAGR',
            'interest_rate': '40% of adults 45+ interested',
            'action_rate': '2-16% actually participate',
        },
        'benefits': {
            'loneliness_reduction': '61%',
            'safety_improvement': '73%',
            'student_savings': '$24,000 annually',
        },
        'demographics': {
            'seniors_vs_children': 'Adults 65+ will outnumber children under 18 by 2034',
            'aging_in_place': '77% of older adults want to age in their current homes',
            'home_equity': 'Baby boomers hold ~$14 trillion in home equity',
        },
        'competitors': {
            'silvernest': {
                'status': 'Transitioned to nonprofit (March 2024)',
                'new_name': 'HomeShareOnline.org',
                'funding': '$4.45M including $3M Series A',
                'matches': '75,000+',
            },
            'nonprofits': [
                {'name': 'HIP Housing', 'location': 'San Mateo County', 'since': '1972', 'annual_housed': '~700 people'},
                {'name': 'HomeShare Vermont', 'experience': '40+ years', 'participants': '400+ active', 'assistance_hours': '39,014 annually'},
                {'name': 'Affordable Living for the Aging', 'location': 'Los Angeles', 'since': '1978', 'matches': '~2,500'},
            ],
        },
    }
    
    context = {
        'nesterly': nesterly_data,
    }
    return render(request, 'companies/home.html', context)


def companies_list(request):
    """Company list page with all delta v companies"""
    # First time visiting? Import companies from Excel
    if Company.objects.count() == 0:
        import_companies_from_excel()
    
    companies = Company.objects.all().order_by('-year', 'name')
    
    # Get distinct years for filter dropdown
    years = Company.objects.exclude(year__isnull=True).values_list('year', flat=True).distinct().order_by('-year')
    
    context = {
        'companies': companies,
        'years': years,
    }
    return render(request, 'companies/companies_list.html', context)


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
    
    # Calculate progress percentage
    progress_percentage = ((company.current_step - 1) / 24) * 100
    
    context = {
        'company': company,
        'steps_by_theme': steps_by_theme,
        'progress_percentage': progress_percentage,
    }
    return render(request, 'companies/company_detail.html', context)


@require_http_methods(["GET"])
def get_companies_api(request):
    """API endpoint to get companies as JSON"""
    companies = Company.objects.all().values('id', 'name', 'year', 'sector')
    return JsonResponse({
        'companies': list(companies)
    })
