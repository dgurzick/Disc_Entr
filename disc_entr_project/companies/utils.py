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
            # Get company name from various possible column names
            company_name = row.get('Company') or row.get('Company Name') or row.get('name')
            
            if pd.isna(company_name):
                continue
                
            company_name = str(company_name).strip()
            
            # Extract all available fields
            year = None
            if 'Year' in df.columns and pd.notna(row.get('Year')):
                try:
                    year = int(row['Year'])
                except (ValueError, TypeError):
                    year = None
            
            tagline = None
            if 'Tagline' in df.columns and pd.notna(row.get('Tagline')):
                tagline = str(row['Tagline']).strip()
            
            description = None
            if 'Description' in df.columns and pd.notna(row.get('Description')):
                description = str(row['Description']).strip()
            
            website = None
            if 'Website' in df.columns and pd.notna(row.get('Website')):
                website = str(row['Website']).strip()
            
            companies_data.append({
                'name': company_name,
                'year': year,
                'tagline': tagline,
                'description': description,
                'website': website,
            })
        
        return companies_data
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return []


def import_companies_from_excel():
    """Import companies from Excel into the database"""
    companies_data = load_companies_from_excel()
    
    created_count = 0
    updated_count = 0
    for company_data in companies_data:
        company, created = Company.objects.update_or_create(
            name=company_data['name'],
            defaults={
                'year': company_data.get('year'),
                'tagline': company_data.get('tagline'),
                'description': company_data.get('description'),
                'website': company_data.get('website'),
            }
        )
        if created:
            created_count += 1
        else:
            updated_count += 1
    
    return created_count
