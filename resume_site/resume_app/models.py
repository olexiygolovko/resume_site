from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=116)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField()
    about = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    company_name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Education(models.Model):
    name_institution = models.CharField(max_length=200)
    speciality = models.CharField(max_length=220)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Language(models.Model):
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=80)

    def __str__(self):
        return self.title


class PortfolioProject(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    scr_shot = models.ImageField()
    url = models.URLField(max_length=320)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=220)
    icon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField(max_length = 255)
    phone = models.CharField(max_length = 80)
    git = models.URLField(max_length=320)
    linkedin = models.URLField(max_length=320)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Resume(models.Model):
    pass


class Slider(models.Model):
    pass

