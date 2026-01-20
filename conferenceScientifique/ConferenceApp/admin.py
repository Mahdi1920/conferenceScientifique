from django.contrib import admin
from .models import *

# Register your models here.

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start_date', 'end_date')
    search_fields = ('name', 'theme', 'location')
    list_filter = ('theme', 'location')
    list_per_page = 1

admin.site.register(Conference, ConferenceAdmin)

#admin.site.register(Submission)
@admin.register(Submission)
class submissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'conference', 'user', 'submission_date', 'status','paid')
    search_fields = ('title', 'user__username', 'conference__name')
    list_filter = ('status', 'paid', 'conference__theme')
    list_per_page = 10
    ordering = ('-submission_date',)
    list_editable = ('status',)

    #fields or fieldsets
    #fields = ('title', 'abstract', 'paper', 'keywords', 'status', 'paid', 'conference', 'user')
    fieldsets = (
        ('Submission Details', {  
            'fields': ('title', 'abstract', 'paper', 'keywords')
        }),
        ('Status Information', {
            'fields': ('status', 'paid')
        }),
        ('Associations', {
            'fields': ('conference', 'user')
        }),
    )
    
    actions = ['set_Paid', 'set_UnPaid']
    def set_Paid(self, request, queryset):
        queryset.update(paid=True)
        self.message_user(request, "Selected submissions have been marked as paid.")
    set_Paid.short_description = "Mark selected submissions as Paid"

    def set_UnPaid(self, request, queryset):
        queryset.update(paid=False)
        self.message_user(request, "Selected submissions have been marked as unpaid.")  
    set_UnPaid.short_description = "Mark selected submissions as Unpaid"
    

admin.site.register(OrganizerCommittee)
