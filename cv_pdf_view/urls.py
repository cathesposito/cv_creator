from django.urls import path
from .views import *

urlpatterns = [
    path('personal_info/pdf/<int:pk>/', PersonalInfoPdfView.as_view(),
         name='personal_info_as_pdf'),
    path('personal_info/update/<int:pk>/', PersonalInfoUpdateView.as_view(),
         name='personal_info_update'),
    path('personal_info', PersonalInfoView.as_view(), name='personal_info'),
    path('job', JobView.as_view(), name='job'),
    path('study', StudyView.as_view(), name='study'),
    path('social_media', SocialMediaView.as_view(), name='social_media'),
    path('language', LanguageView.as_view(), name='language'),
    path('soft_skill', SoftSkillView.as_view(), name='soft_skill'),
    path('hard_skill', HardSkillView.as_view(), name='hard_skill'),
]
