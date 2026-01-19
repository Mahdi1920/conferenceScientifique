from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Conference)
admin.site.register(OrganizerCommittee)
admin.site.register(Submission)