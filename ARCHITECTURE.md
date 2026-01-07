# Architecture & Design Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    DISCIPLINED ENTREPRENEURSHIP PLATFORM     │
└─────────────────────────────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
    ┌───▼────┐        ┌──────▼──────┐      ┌─────▼─────┐
    │  VIEWS │        │   MODELS    │      │  TEMPLATES│
    └────────┘        └─────────────┘      └───────────┘
        │                    │                    │
        │ landing_page       │ Company            │ landing.html
        │ company_detail     │ EntrepreneurialStep│ company_detail.html
        │ get_companies_api  │                    │
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
    ┌───▼────────┐   ┌───────▼──────┐   ┌────────▼──────┐
    │   URLS     │   │   DATABASE   │   │  STATIC FILES │
    └────────────┘   └──────────────┘   └───────────────┘
        │              db.sqlite3           css/style.css
        │              - Companies          js/main.js
        │              - Steps
        │
```

## Data Flow

### 1. Landing Page Flow
```
User visits /
    ↓
Django checks if companies exist in DB
    ├─ If empty: load from Excel file
    ↓
Render landing.html with all companies
    ├─ Display company cards
    ├─ Search/Filter functionality
    ├─ Framework overview (6 themes)
    ↓
User clicks company card
    ↓
Redirect to company detail page
```

### 2. Company Detail Page Flow
```
User visits /company/<id>/
    ↓
Fetch company from database
    ↓
Fetch all 24 steps for that company
    ↓
Group steps by theme (1-6)
    ↓
Render company_detail.html with:
    - Company information
    - Progress bar (current step/24)
    - 24 Steps organized by theme
    - Each step with status, notes, completion date
    ↓
User can click admin links to edit
```

### 3. Data Import Flow
```
run: python manage.py init_24steps
    ↓
Read Excel file (MIT_DeltaV_Companies_2017-2025.xlsx)
    ↓
For each company in Excel:
    ├─ Create Company record in database
    ├─ Skip if already exists
    ↓
For each company in database:
    ├─ Create 24 EntrepreneurialStep records
    ├─ Assign to proper theme
    ├─ Set initial status to "Not Started"
    ├─ Skip if already exists
    ↓
Display summary of created records
```

## Database Schema

### Company Table
```
┌─────────────────────────────────┐
│         COMPANY                 │
├─────────────────────────────────┤
│ id (PK)                         │
│ name (unique, CharField)        │
│ year (IntegerField, nullable)   │
│ sector (CharField, nullable)    │
│ description (TextField)         │
│ contact_info (TextField)        │
│ website (URLField, nullable)    │
│ current_step (IntegerField)     │
│ notes (TextField)               │
│ created_at (DateTimeField)      │
│ updated_at (DateTimeField)      │
└─────────────────────────────────┘
```

### EntrepreneurialStep Table
```
┌────────────────────────────────────┐
│     ENTREPRENEURIAL STEP           │
├────────────────────────────────────┤
│ id (PK)                            │
│ company_id (FK) → Company          │
│ theme (CharField)                  │
│ step_number (IntegerField, 1-24)   │
│ step_title (CharField)             │
│ description (TextField)            │
│ status (CharField)                 │
│   - not_started                    │
│   - in_progress                    │
│   - completed                      │
│ notes (TextField)                  │
│ completion_date (DateField)        │
│ created_at (DateTimeField)         │
│ updated_at (DateTimeField)         │
│ unique_together: (company, step)   │
└────────────────────────────────────┘
```

## The 24 Steps Framework

### Organization
```
6 THEMES
    │
    ├─ THEME 1: Who Is Your Customer? (5 steps)
    │   ├─ Step 1: Market Segmentation
    │   ├─ Step 2: Select Beachhead Market
    │   ├─ Step 3: Build End User Profile
    │   ├─ Step 4: Calculate TAM
    │   └─ Step 5: Profile the Persona
    │
    ├─ THEME 2: What Can You Do for Your Customer? (3 steps)
    │   ├─ Step 6: Full Life Cycle Use Case
    │   ├─ Step 7: High-Level Product Spec
    │   └─ Step 8: Quantify Value Proposition
    │
    ├─ THEME 3: How Does Your Customer Acquire Your Product? (3 steps)
    │   ├─ Step 9: Identify Next 10 Customers
    │   ├─ Step 10: Define Your Core
    │   └─ Step 11: Chart Competitive Position
    │
    ├─ THEME 4: How Do You Make Money? (8 steps)
    │   ├─ Step 12: Determine DMU
    │   ├─ Step 13: Map Acquisition Process
    │   ├─ Step 14: Calculate Follow-On TAM
    │   ├─ Step 15: Design Business Model
    │   ├─ Step 16: Set Pricing Framework
    │   ├─ Step 17: Calculate LTV
    │   ├─ Step 18: Map Sales Process
    │   └─ Step 19: Calculate COCA
    │
    ├─ THEME 5: How Do You Design and Build Your Product? (4 steps)
    │   ├─ Step 20: Identify Key Assumptions
    │   ├─ Step 21: Test Key Assumptions
    │   ├─ Step 22: Define MVBP
    │   └─ Step 23: Dogs Will Eat Dog Food
    │
    └─ THEME 6: How Do You Scale? (1 step)
        └─ Step 24: Develop Product Plan
```

## User Workflows

### Workflow 1: Initial Setup
```
1. Install Python and dependencies
   └─ python -m venv venv
   └─ pip install -r requirements.txt

2. Initialize database
   └─ python manage.py migrate

3. Import companies and steps
   └─ python manage.py init_24steps

4. Run server
   └─ python manage.py runserver

5. Access application
   └─ http://localhost:8000/
```

### Workflow 2: Tracking Progress
```
1. View landing page
   └─ See all companies from Excel

2. Search for specific company
   └─ Use search bar to filter

3. Click company card
   └─ View company details

4. View 24 Steps progress
   └─ See steps organized by theme
   └─ Check status of each step

5. Go to admin to update
   └─ Click "Edit Company" or "Manage Steps"
   └─ Update step status
   └─ Add completion dates and notes

6. Track overall progress
   └─ Progress bar shows current_step/24
```

### Workflow 3: Managing Company Data
```
1. Access admin panel
   └─ http://localhost:8000/admin/

2. Select Companies or EntrepreneurialSteps

3. Update information
   ├─ Edit company details (sector, website, notes)
   ├─ Update step status
   ├─ Add completion dates
   └─ Document progress notes

4. Save changes
   └─ Updated data automatically reflected on front end
```

## Technology Stack

### Backend
- **Framework**: Django 4.2.9
  - ORM for database operations
  - Admin interface for data management
  - URL routing and view handling
  - Template rendering

### Database
- **SQLite3** (default, can be switched to PostgreSQL/MySQL)
  - Lightweight and perfect for development
  - No additional setup required

### Data Import
- **pandas** 2.1.4
  - Read Excel files
  - Data manipulation and cleaning
- **openpyxl** 3.10.10
  - Low-level Excel file reading
  - Dependency of pandas

### Frontend
- **HTML5**
  - Semantic structure
  - Responsive meta tags

- **CSS3**
  - Modern flexbox and grid layouts
  - CSS variables for theming
  - Media queries for responsiveness
  - Gradients and transitions

- **Vanilla JavaScript**
  - No framework dependencies
  - Smooth scrolling
  - Intersection Observer for animations
  - Search functionality

### Development
- **Python 3.8+**
- **pip** for package management
- **Virtual environments** for isolation

## Key Features

### 1. Company Management
- Load companies from Excel file
- Store company metadata
- Track current progress step
- Maintain contact information

### 2. Progress Tracking
- 24 steps framework implementation
- 6 themed categories
- Status tracking (Not Started, In Progress, Completed)
- Completion date recording
- Notes and documentation

### 3. User Interface
- Responsive design (mobile-friendly)
- Company search functionality
- Visual progress indicators
- Theme-based organization
- Admin panel for management

### 4. Data Persistence
- SQLite database
- Automatic data relationships (Company → Steps)
- Unique constraints (no duplicate companies or steps)
- Timestamp tracking (created_at, updated_at)

## Scalability Considerations

### Current Implementation
- SQLite (single file, suitable for ~1000 companies)
- Single server deployment

### For Production Scaling
1. **Database**: PostgreSQL or MySQL
2. **Hosting**: Heroku, AWS, Digital Ocean
3. **Caching**: Redis for frequently accessed data
4. **Frontend**: Consider Django template caching
5. **Static Files**: CDN (CloudFront, CloudFlare)
6. **Monitoring**: Application monitoring and logging

## Future Enhancement Ideas

1. **Analytics Dashboard**
   - Company progress statistics
   - Step completion rates
   - Timeline visualization

2. **Collaboration Features**
   - Team assignments
   - Comments on steps
   - File attachments

3. **Advanced Tracking**
   - Financial metrics
   - Customer data
   - Investment tracking

4. **Reporting**
   - PDF export of progress
   - Excel reports
   - Custom report generation

5. **API Expansion**
   - RESTful API
   - GraphQL endpoint
   - Mobile app backend

6. **Integrations**
   - Slack notifications
   - Google Drive/Sheets sync
   - Calendar integration

---

This architecture provides a solid foundation for tracking entrepreneurial ventures through the 24 Steps framework while remaining simple enough for easy maintenance and updates.
