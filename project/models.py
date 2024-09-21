from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Projet(models.Model):
    titre = models.CharField(max_length=100)
    link = models.URLField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='projects/thumbnails/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('in progress', 'In Progress'), ('completed', 'Completed'), ('archived', 'Archived')], default='in progress')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.titre
