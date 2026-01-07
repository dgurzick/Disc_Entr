# Disciplined Entrepreneurship Platform

A Django web application for tracking entrepreneurial ventures through Bill Aulet's **24 Steps of Disciplined Entrepreneurship** framework from MIT.

## Overview

This platform allows you to:
- Load company data from your Excel file (MIT_DeltaV_Companies_2017-2025.xlsx)
- Track progress through the 24 Steps framework across 6 themes
- View company details and entrepreneurial step status
- Manage and update company information and progress

## Project Structure

```
disc_entr_project/
├── manage.py                 # Django management script
├── disc_entr_project/        # Main Django project settings
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL configuration
│   ├── wsgi.py              # WSGI config
│   └── asgi.py              # ASGI config
├── companies/               # Main app for managing companies
│   ├── models.py            # Company and EntrepreneurialStep models
│   ├── views.py             # View logic
│   ├── urls.py              # App URL patterns
│   ├── admin.py             # Django admin configuration
│   ├── utils.py             # Utility functions for Excel import
│   └── management/
│       └── commands/
│           └── init_24steps.py  # Command to initialize 24 steps
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   └── companies/           # Company-specific templates
│       ├── landing.html     # Landing page with company selector
│       └── company_detail.html  # Individual company detail page
├── static/                  # Static files
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   └── js/
│       └── main.js          # Main JavaScript file
└── db.sqlite3               # SQLite database (created after migrations)
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Create Virtual Environment

```bash
cd disc_entr_project
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Migrations

```bash
python manage.py migrate
```

### Step 4: Initialize 24 Steps Data

This command will:
1. Load companies from your Excel file
2. Create the 24 Steps framework for each company

```bash
python manage.py init_24steps
```

### Step 5: Create Superuser (Optional)

To access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 6: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://localhost:8000/`

## Usage

### Landing Page
- Visit the home page to see all companies loaded from your Excel file
- Use the search bar to filter companies by name or year
- Click on any company card to view detailed information

### Company Detail Page
- View complete company information
- See progress through the 24 Steps framework
- Steps are organized by theme
- Each step shows status (Not Started, In Progress, Completed)

### Admin Panel
Access Django admin at: `http://localhost:8000/admin/`

In the admin panel, you can:
- **Edit Companies**: Update company details, sector, website, notes, etc.
- **Manage Steps**: Update the status of each entrepreneurial step
- **Add Notes**: Document progress and decisions for each step
- **Track Completion**: Record completion dates for steps

## The 24 Steps Framework

### Theme 1: Who Is Your Customer?
1. Market Segmentation
2. Select a Beachhead Market
3. Build an End User Profile
4. Calculate Total Addressable Market (TAM)
5. Profile the Persona

### Theme 2: What Can You Do for Your Customer?
6. Full Life Cycle Use Case
7. High-Level Product Specification
8. Quantify the Value Proposition

### Theme 3: How Does Your Customer Acquire Your Product?
9. Identify Your Next 10 Customers
10. Define Your Core
11. Chart Your Competitive Position

### Theme 4: How Do You Make Money?
12. Determine the Customer's Decision-Making Unit (DMU)
13. Map the Process to Acquire a Paying Customer
14. Calculate TAM for Follow-On Markets
15. Design a Business Model
16. Set Your Pricing Framework
17. Calculate Lifetime Value (LTV)
18. Map the Sales Process
19. Calculate Cost of Customer Acquisition (COCA)

### Theme 5: How Do You Design and Build Your Product?
20. Identify Key Assumptions
21. Test Key Assumptions
22. Define Minimum Viable Business Product (MVBP)
23. Show That the Dogs Will Eat the Dog Food

### Theme 6: How Do You Scale?
24. Develop a Product Plan

## Features

### Current Features
- ✅ Company listing and search
- ✅ Landing page with company selector
- ✅ Company detail pages
- ✅ 24 Steps framework tracking
- ✅ Progress visualization
- ✅ Admin interface for management
- ✅ Excel file integration
- ✅ Responsive design

### Planned Features
- Analytics dashboard
- Activity timeline
- Export reports (PDF/Excel)
- Team collaboration features
- Investment tracking
- Customer feedback integration

## Database Models

### Company
Stores company information including:
- Name (unique)
- Year
- Sector
- Description
- Contact information
- Website
- Current step (1-24)
- Custom notes
- Timestamps

### EntrepreneurialStep
Tracks progress through the 24 steps:
- Company (foreign key)
- Step number (1-24)
- Theme classification
- Title and description
- Status (Not Started, In Progress, Completed)
- Notes
- Completion date
- Timestamps

## Configuration

Edit `disc_entr_project/settings.py` to customize:

```python
# Excel file location (automatically set to parent directory)
EXCEL_FILE_PATH = os.path.join(os.path.dirname(BASE_DIR), 'MIT_DeltaV_Companies_2017-2025.xlsx')

# Database location
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files location
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

## Troubleshooting

### Excel File Not Found
Make sure `MIT_DeltaV_Companies_2017-2025.xlsx` is in the parent directory of `disc_entr_project/`

### Port Already in Use
If port 8000 is busy, use:
```bash
python manage.py runserver 8001
```

### Database Migration Errors
Reset the database:
```bash
# Delete db.sqlite3 file
python manage.py migrate
python manage.py init_24steps
```

## API Endpoints

### Get Companies List (JSON)
```
GET /api/companies/
```

Returns JSON with all companies and basic information.

## Customization

### Adding Fields to Companies
Edit `companies/models.py` and add fields to the `Company` model:

```python
class Company(models.Model):
    # Existing fields...
    your_new_field = models.CharField(max_length=255, blank=True)
```

Then run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Customizing Styling
Edit `static/css/style.css` to modify colors, fonts, and layouts.

## Requirements

- Django==4.2.9
- openpyxl==3.10.10 (Excel file reading)
- pandas==2.1.4 (Data manipulation)
- python-dotenv==1.0.0 (Environment variables)

## License

This project is based on Bill Aulet's Disciplined Entrepreneurship framework from MIT.

## Support

For issues or questions, contact the development team.

---

**Created for MIT DeltaV 2017-2025 Companies**
