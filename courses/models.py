from django.db import models
from django.contrib.auth.models import  User
from django.db.models import fields, query
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='moudules', on_delete=CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course']) # ordering with respect to course field

    class Meta:
        ordering = ['order'] # default ordering

    def __str__(self) -> str:
        return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in':('text',
    'video',
    'image',
    'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module']) # ordering with respect to module field
    
    class Meta:
        ordering = ['order'] # default ordering


class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Images(ItemBase):
    file = models.ImageField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()

