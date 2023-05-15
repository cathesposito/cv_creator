from django.contrib import admin
from .models import PersonalInfo, Job, SocialMedia, Study, Language, SoftSkill, HardSkill

# Register your models here.

admin.site.register(PersonalInfo)
admin.site.register(Job)
admin.site.register(Study)
admin.site.register(SocialMedia)
admin.site.register(Language)
admin.site.register(SoftSkill)
admin.site.register(HardSkill)