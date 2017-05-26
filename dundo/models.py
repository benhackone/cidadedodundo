from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.urlresolvers import reverse



class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.nome


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Noticia(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    autor = models.ForeignKey(User, related_name='dundo_noticias')
    fonte_noticia = models.CharField(max_length=250, null=True, blank=True)
    fonte_url = models.URLField(blank=True)
    noticia_texto = models.TextField(max_length=15000)
    imagem_url = models.URLField(blank=True)

    # Não obriga a definir categoria por causa do blank=True
    categoria = models.ForeignKey(Categoria, related_name='noticias',  null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # The Dahl-specific manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('dundo:noticia_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])
