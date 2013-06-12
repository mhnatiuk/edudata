from django.contrib import admin
import research_db.models


class DataframeInline(admin.StackedInline):
    model = research_db.models.Dataframe
    extra =3

class ResearchProjectAdmin(admin.ModelAdmin):
    inlines = [DataframeInline]

admin.site.register(research_db.models.ResearchProject, ResearchProjectAdmin)
admin.site.register(research_db.models.Dataframe)
admin.site.register(research_db.models.Product)
admin.site.register(research_db.models.ResearchKeyword)
admin.site.register(research_db.models.DataframeKeyword)
admin.site.register(research_db.models.Team)

