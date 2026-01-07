import pandas as pd
from django.conf import settings
from .models import Company


def load_companies_from_excel():
    """Load company data from Excel file"""
    excel_file = settings.EXCEL_FILE_PATH
    
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)
        
        companies_data = []
        for idx, row in df.iterrows():
            # Adjust column names based on your actual Excel structure
            company_name = row.get('Company Name') or row.get('name') or row.get('Company')
            
            if pd.isna(company_name):
                continue
                
            company_name = str(company_name).strip()
            
            # Try to extract year if available
            year = None
            if 'Year' in df.columns:
                year = int(row['Year']) if pd.notna(row['Year']) else None
            
            companies_data.append({
                'name': company_name,
                'year': year,
            })
        
        return companies_data
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return []


def import_companies_from_excel():
    """Import companies from Excel into the database"""
    companies_data = load_companies_from_excel()
    
    created_count = 0
    for company_data in companies_data:
        company, created = Company.objects.get_or_create(
            name=company_data['name'],
            defaults={'year': company_data.get('year')}
        )
        if created:
            created_count += 1
    
    return created_count
