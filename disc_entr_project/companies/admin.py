from django.contrib import admin
from .models import Company, EntrepreneurialStep


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'current_step', 'created_at')
    list_filter = ('year', 'current_step')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(EntrepreneurialStep)
class EntrepreneurialStepAdmin(admin.ModelAdmin):
    list_display = ('company', 'step_number', 'step_title', 'status', 'completion_date')
    list_filter = ('theme', 'status', 'company')
    search_fields = ('step_title', 'company__name')
    readonly_fields = ('created_at', 'updated_at')
