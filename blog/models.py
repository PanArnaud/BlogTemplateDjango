from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Titre")
    slug = models.SlugField(max_length=100, db_index=True, verbose_name="Slug")

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return('view_blog_category', None, {'slug': self.slug})


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")
    body = models.TextField(default="", verbose_name="Contenu")
    posted = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name="Date de creation")
    category = models.ForeignKey('blog.Category', default=1, verbose_name="Categorie")
    author = models.ForeignKey(User, default=1, verbose_name="Auteur")
    photos = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="Image(s)")

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return('view_blog_post', None, {'slug': self.slug})