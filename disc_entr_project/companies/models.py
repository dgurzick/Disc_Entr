from django.db import models


class Company(models.Model):
    """Model to store company information from Excel"""
    name = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()
    # Add other fields based on your Excel structure
    # You can customize these after reviewing the Excel file
    sector = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    # Fields for 24 Steps Framework
    current_step = models.IntegerField(default=1)  # 1-24
    notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f"{self.name} ({self.year})"


class EntrepreneurialStep(models.Model):
    """Model to track progress through the 24 Steps framework"""
    THEMES = [
        ('theme1', 'Theme 1: Who Is Your Customer?'),
        ('theme2', 'Theme 2: What Can You Do for Your Customer?'),
        ('theme3', 'Theme 3: How Does Your Customer Acquire Your Product?'),
        ('theme4', 'Theme 4: How Do You Make Money?'),
        ('theme5', 'Theme 5: How Do You Design and Build Your Product?'),
        ('theme6', 'Theme 6: How Do You Scale?'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='steps')
    theme = models.CharField(max_length=10, choices=THEMES)
    step_number = models.IntegerField()  # 1-24
    step_title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('not_started', 'Not Started'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
        ],
        default='not_started'
    )
    notes = models.TextField(blank=True)
    completion_date = models.DateField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['step_number']
        unique_together = ('company', 'step_number')

    def __str__(self):
        return f"{self.company.name} - Step {self.step_number}: {self.step_title}"
