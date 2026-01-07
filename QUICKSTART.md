# Quick Start Guide

## Getting Started with the Disciplined Entrepreneurship Platform

### Prerequisites
- Python 3.8 or higher installed
- Windows, macOS, or Linux

### Step-by-Step Setup

#### 1. Navigate to the Project Directory
```bash
cd disc_entr_project
```

#### 2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command line prompt.

#### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

This will install:
- Django 4.2.9
- openpyxl (for reading Excel files)
- pandas (for data manipulation)
- python-dotenv (for environment variables)

#### 4. Run Database Migrations
```bash
python manage.py migrate
```

This creates the SQLite database (`db.sqlite3`) with all necessary tables.

#### 5. Load Companies and Initialize 24 Steps Framework
```bash
python manage.py init_24steps
```

This command will:
- Read your Excel file (MIT_DeltaV_Companies_2017-2025.xlsx)
- Create a database entry for each company
- Set up all 24 steps for each company

#### 6. (Optional) Create an Admin Account
```bash
python manage.py createsuperuser
```

Follow the prompts to create a username, email, and password.

#### 7. Start the Development Server
```bash
python manage.py runserver
```

The server will start and display:
```
Starting development server at http://127.0.0.1:8000/
```

#### 8. Access the Application

**Landing Page (Company Selector)**
- URL: http://localhost:8000/
- Shows all companies from your Excel file
- Search functionality to filter by name or year

**Company Detail Page**
- Click on any company card to view details
- See the 24 Steps framework with progress tracking

**Admin Panel** (if you created a superuser)
- URL: http://localhost:8000/admin/
- Login with your superuser credentials
- Manage companies and step progress
- Update company information
- Track step completion dates

### Common Commands

```bash
# Run the development server
python manage.py runserver

# Run on a different port
python manage.py runserver 8001

# Create a superuser
python manage.py createsuperuser

# Apply database migrations
python manage.py migrate

# Make database migrations after model changes
python manage.py makemigrations

# Access Django shell (Python REPL with Django)
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic

# Re-import companies and reset steps
python manage.py init_24steps
```

### Stop the Server

Press `Ctrl + C` in the terminal.

### Deactivate Virtual Environment

```bash
deactivate
```

### Troubleshooting

**ModuleNotFoundError: No module named 'django'**
- Make sure you've activated the virtual environment
- Make sure you've run `pip install -r requirements.txt`

**Port 8000 already in use**
```bash
python manage.py runserver 8001
```

**Excel file not found**
- Make sure `MIT_DeltaV_Companies_2017-2025.xlsx` is in the parent directory
- The app will still work without the Excel file, but companies won't be loaded

**No companies showing up**
- Run `python manage.py init_24steps` again
- Check that the Excel file is in the correct location

### Next Steps

Once the application is running:

1. **Explore the Landing Page**
   - Search for companies
   - Click on company cards to view details

2. **Use the Admin Panel**
   - Update company information
   - Track progress through the 24 Steps
   - Add notes and completion dates

3. **Customize the Framework**
   - Edit company sectors
   - Add website URLs
   - Document progress notes

4. **Review the Code**
   - Check `companies/models.py` for data structure
   - Review `companies/views.py` for business logic
   - Examine templates for frontend design

### Project Structure Reference

```
disc_entr_project/
├── manage.py                 # Django management script
├── disc_entr_project/        # Project configuration
├── companies/                # Main application
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── urls.py              # URL routes
│   └── management/commands/  # Custom commands
├── templates/                # HTML templates
├── static/                   # CSS and JavaScript
└── db.sqlite3               # Database (created after migrate)
```

### File Locations

- **Main App Code**: `disc_entr_project/companies/`
- **HTML Templates**: `disc_entr_project/templates/`
- **CSS Styles**: `disc_entr_project/static/css/style.css`
- **JavaScript**: `disc_entr_project/static/js/main.js`
- **Database**: `disc_entr_project/db.sqlite3`
- **Excel Data**: `../MIT_DeltaV_Companies_2017-2025.xlsx`

---

For detailed documentation, see the main [README.md](README.md) file.
