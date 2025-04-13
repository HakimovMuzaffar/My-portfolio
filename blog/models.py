from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=200)
    client = models.CharField(max_length=100)
    date = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField(verbose_name='Content of product')
    project_url = models.URLField()
    slug = models.SlugField(unique=True, null=True)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def get_first_photo(self):
        if self.images:
            try:
                return self.images.first().image.url
            except:
                return 'https://img.freepik.com/premium-vector/no-photo-available-vector-icon-default-image-symbol-picture-coming-soon-web-site-mobile-app_87543-18055.jpg'
        else:
            return 'https://img.freepik.com/premium-vector/no-photo-available-vector-icon-default-image-symbol-picture-coming-soon-web-site-mobile-app_87543-18055.jpg'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Product pk={self.pk}, name={self.name}, client={self.client}'

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Gallery(models.Model):
    image = models.ImageField(upload_to='project/', verbose_name='Rasmlar')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'
