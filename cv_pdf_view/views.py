from django.views.generic.edit import UpdateView
from .models import PersonalInfo, Job, Study, SocialMedia, SoftSkill, HardSkill, Language
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from .pdf_cv_view import PdfCreatorPort


class PersonalInfoView(View):
    def get(self, request, *args, **kwargs):
        data = PersonalInfo.objects.all()

        title = "User Information"

        dict_part = PersonalInfo.objects.values_list().all()

        field_names = [
            field.name for field in PersonalInfo._meta.get_fields()]

        table_headers = [i.capitalize().replace('_', ' ').title()
                         for i in field_names]

        return render(
            request, 'info_view.html', {'title': title, 'data': data, 'table_headers': table_headers, 'dict_part': dict_part})


class PersonalInfoPdfView(View):
    def get(self, request, *args, **kwargs):

        pdf = PdfCreatorPort().build_pdf()

        response = HttpResponse(content_type='application/pdf')
        response.write(pdf)

        return response


class PersonalInfoUpdateView(UpdateView):
    model = PersonalInfo
    fields = '__all__'
    template_name = 'update_info_view.html'
    success_url = '/contact_info/'
    success_message = "Contact info were updated successfully"


class JobView(View):
    def get(self, request, *args, **kwargs):
        data = Job.objects.all()

        title = "Job"

        dict_part = Job.objects.values_list().all()

        field_names = [
            field.name for field in Job._meta.get_fields()]

        table_headers = [i.capitalize().replace('_', ' ').title()
                         for i in field_names]

        return render(
            request, 'other_models_view.html', {'title': title, 'data': data, 'table_headers': table_headers, 'dict_part': dict_part})
    
class StudyView(View):
    def get(self, request, *args, **kwargs):
        data = Study.objects.all()

        title = "Study"

        dict_part = Study.objects.values_list().all()

        field_names = [
            field.name for field in Study._meta.get_fields()]

        table_headers = [i.capitalize().replace('_', ' ').title()
                         for i in field_names]

        return render(
            request, 'other_models_view.html', {'title': title, 'data': data, 'table_headers': table_headers, 'dict_part': dict_part})

class SocialMediaView(View):
    def get(self, request, *args, **kwargs):
        data = SocialMedia.objects.all()

        title = "Social Media"

        dict_part = SocialMedia.objects.values_list().all()

        field_names = [
            field.name for field in SocialMedia._meta.get_fields()]

        table_headers = [i.capitalize().replace('_', ' ').title()
                         for i in field_names]

        return render(
            request, 'other_models_view.html', {'title': title, 'data': data, 'table_headers': table_headers, 'dict_part': dict_part})

class LanguageView(View):
    def get(self, request, *args, **kwargs):
        data = Language.objects.all()

        title = "Language"

        dict_part = Language.objects.values_list().all()

        field_names = [
            field.name for field in Language._meta.get_fields()]

        table_headers = [i.capitalize().replace('_', ' ').title()
                         for i in field_names]

        return render(
            request, 'other_models_view.html', {'title': title, 'data': data, 'table_headers': table_headers, 'dict_part': dict_part})

class SoftSkillView(View):
    def get(self, request, *args, **kwargs):
        data = SoftSkill.objects.all()

        title = "Soft Skill"

        dict_part = SoftSkill.objects.values_list().all()

        field_names = [
            field.name for field in SoftSkill._meta.get_fields()]

        table_headers = [i.capitalize().replace('_', ' ').title()
                         for i in field_names]

        return render(
            request, 'other_models_view.html', {'title': title, 'data': data, 'table_headers': table_headers, 'dict_part': dict_part})

class HardSkillView(View):
    def get(self, request, *args, **kwargs):
        data = HardSkill.objects.all()

        title = "Hard Skill"

        dict_part = HardSkill.objects.values_list().all()

        field_names = [
            field.name for field in HardSkill._meta.get_fields()]

        table_headers = [i.capitalize().replace('_', ' ').title()
                         for i in field_names]

        return render(
            request, 'other_models_view.html', {'title': title, 'data': data, 'table_headers': table_headers, 'dict_part': dict_part})
