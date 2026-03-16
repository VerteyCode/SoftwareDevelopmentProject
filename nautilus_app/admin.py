from django.contrib import admin

from .models import NautilusTeamModel, NautilusReviewModel, NautilusConsultationModel

admin.site.register(NautilusTeamModel)
admin.site.register(NautilusReviewModel)
admin.site.register(NautilusConsultationModel)