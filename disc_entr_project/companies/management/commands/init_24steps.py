from django.core.management.base import BaseCommand
from companies.models import EntrepreneurialStep
from companies.utils import import_companies_from_excel


STEPS_DATA = [
    # Theme 1: Who Is Your Customer?
    (1, 'theme1', 'Market Segmentation', 'Brainstorm and identify potential customer segments, breaking down the broad market into distinct groups with similar needs.'),
    (2, 'theme1', 'Select a Beachhead Market', 'Choose one specific segment to focus on first, small enough to win but large enough to matter.'),
    (3, 'theme1', 'Build an End User Profile', 'Create a detailed description of who will actually use your product, including demographics, behaviors, and priorities.'),
    (4, 'theme1', 'Calculate Total Addressable Market (TAM)', 'Estimate the annual revenue opportunity if you captured 100% of your beachhead market.'),
    (5, 'theme1', 'Profile the Persona', 'Develop a single, specific representative of your target customer with a name, photo, and detailed characteristics.'),
    
    # Theme 2: What Can You Do for Your Customer?
    (6, 'theme2', 'Full Life Cycle Use Case', 'Map out exactly how your customer will discover, acquire, use, and potentially recommend your product.'),
    (7, 'theme2', 'High-Level Product Specification', 'Define what your product does (not how) in terms of functionality and benefits.'),
    (8, 'theme2', 'Quantify the Value Proposition', 'Calculate the concrete, measurable value your solution delivers to the customer.'),
    
    # Theme 3: How Does Your Customer Acquire Your Product?
    (9, 'theme3', 'Identify Your Next 10 Customers', 'Find real prospects beyond your persona who would buy your product.'),
    (10, 'theme3', 'Define Your Core', 'Articulate what makes your venture uniquely positioned to win—your unfair advantage.'),
    (11, 'theme3', 'Chart Your Competitive Position', 'Map where you stand against alternatives on the dimensions customers care about most.'),
    
    # Theme 4: How Do You Make Money?
    (12, 'theme4', 'Determine the Customer\'s Decision-Making Unit (DMU)', 'Identify everyone involved in the purchase decision: champion, influencer, economic buyer, etc.'),
    (13, 'theme4', 'Map the Process to Acquire a Paying Customer', 'Outline each step from awareness to purchase, including timeline and requirements.'),
    (14, 'theme4', 'Calculate TAM for Follow-On Markets', 'Estimate revenue potential in adjacent markets you\'ll expand into after winning your beachhead.'),
    (15, 'theme4', 'Design a Business Model', 'Determine how you\'ll capture value (licensing, subscription, product sale, etc.).'),
    (16, 'theme4', 'Set Your Pricing Framework', 'Establish pricing strategy based on value delivered and willingness to pay.'),
    (17, 'theme4', 'Calculate Lifetime Value (LTV)', 'Estimate total revenue from an average customer over the entire relationship.'),
    (18, 'theme4', 'Map the Sales Process', 'Define how you\'ll actually sell, including channels, sales cycle, and required resources.'),
    (19, 'theme4', 'Calculate Cost of Customer Acquisition (COCA)', 'Determine what you\'ll spend in marketing and sales to acquire each customer.'),
    
    # Theme 5: How Do You Design and Build Your Product?
    (20, 'theme5', 'Identify Key Assumptions', 'List the critical hypotheses underlying your business that must be true for success.'),
    (21, 'theme5', 'Test Key Assumptions', 'Design low-cost experiments to validate or invalidate your assumptions before building.'),
    (22, 'theme5', 'Define Minimum Viable Business Product (MVBP)', 'Specify the smallest version of your product that delivers enough value for customers to pay.'),
    (23, 'theme5', 'Show That the Dogs Will Eat the Dog Food', 'Demonstrate actual customer willingness to pay through real transactions or commitments.'),
    
    # Theme 6: How Do You Scale?
    (24, 'theme6', 'Develop a Product Plan', 'Create a roadmap for evolving your product to capture your beachhead and expand into follow-on markets.'),
]


class Command(BaseCommand):
    help = 'Initialize the 24 Steps of Disciplined Entrepreneurship for all companies'

    def handle(self, *args, **options):
        # Import companies from Excel
        imported_count = import_companies_from_excel()
        self.stdout.write(self.style.SUCCESS(f'Imported {imported_count} new companies from Excel'))

        # Create steps for each company
        from companies.models import Company
        companies = Company.objects.all()
        steps_created = 0
        
        for company in companies:
            for step_number, theme, title, description in STEPS_DATA:
                step, created = EntrepreneurialStep.objects.get_or_create(
                    company=company,
                    step_number=step_number,
                    defaults={
                        'theme': theme,
                        'step_title': title,
                        'description': description,
                    }
                )
                if created:
                    steps_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {steps_created} new entrepreneurial steps'))
        self.stdout.write(self.style.SUCCESS('Successfully initialized the 24 Steps framework!'))
