from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                    PermissionsMixin
from django.conf import settings
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth import get_user_model
from django.db import connection
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "email"


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.title

class ProjectType(models.Model):
    """Tag to be used for a project"""
    FIELD = [
        ('data','Data Science'),
        ('web','Full Stack'),
    ]
    type = models.CharField(choices=FIELD, default='data', max_length=100)

    def __str__(self):
        return self.type

class Project(models.Model):
    FIELD = [
        ('data','DataScience'),
        ('web','FullStack'),
    ]
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='My Project')
    description = models.TextField(default="ADMIN MSG: Customisation Required in this field.")
    started_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField()
    type= models.ForeignKey(ProjectType, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
    def save(self, *args, **kwargs):
        self.started_by = self.request.user
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.description, lexer, formatter)
        super(Project, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class Article(models.Model):
    """Article model here which will be reviewed content / project / other"""


class MachineLearningModelType(models.Model):
    """Tag to be used for a ml-model"""
    FIELD = [
        ('clust','Clusturing'),
        ('class','Classification'),
        ('reg','Regression'),
    ]
    type = models.CharField(choices=FIELD, default='clust', max_length=100)
    def __str__(self):
        return self.type

class MachineLearningModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False, default='My Machine Learning Model')
    code = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.ManyToManyField("MachineLearningModelType")
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField()
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(MachineLearningModel, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
