from django.db import models

# Create your models here.


class PersonalInfo(models.Model):
    class Meta:
        verbose_name_plural = "Personal Information"

    name = models.CharField(max_length=500)

    picture = models.ImageField(upload_to='user')

    image = models.ImageField(upload_to='images')

    position = models.CharField(max_length=500)

    address = models.CharField(max_length=500)

    phone = models.CharField(max_length=500)

    email = models.CharField(max_length=500)

    resume_objective = models.TextField()


    def __str__(self):
        return f"Name {self.name}"


class Job(models.Model):
    title = models.CharField(max_length=500)

    location = models.CharField(max_length=500)

    start = models.DateField()

    end = models.DateField(null=True, blank=True)

    current = models.BooleanField(null=True)

    description = models.TextField()

    soft_skills = models.CharField(max_length=500)

    hard_skills = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title}"


class Study(models.Model):

    class Meta:
        verbose_name_plural = "Studies"

    title = models.CharField(max_length=500)

    location = models.CharField(max_length=500)

    start = models.DateField()

    end = models.DateField(null=True, blank=True)

    current = models.BooleanField(blank=True)

    description = models.TextField()

    description2 = models.TextField(blank=True, null=True)

    skills = models.TextField()

    def __str__(self):
        return f"Study {self.title}"


class SocialMedia(models.Model):
    path = models.URLField()

    def __str__(self):
        return f"{self.path}"


class Language(models.Model):
    language = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.language}"


class SoftSkill(models.Model):
    skill = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.skill}"


class HardSkill(models.Model):
    skill = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.skill}"


class Company(models.Model):
    position = models.TextField()

    name = models.TextField(null=True)

    def __str__(self):
        return f"{self.name}"
    
class CoverLetter(models.Model):
    resume = models.TextField()

    resume2 = models.TextField(null=True)

    resume3 = models.TextField(null=True)

    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.resume}"
