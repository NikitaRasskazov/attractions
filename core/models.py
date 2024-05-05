from django.db import models


class Attractions(models.Model):
    name = models.CharField('название', max_length=255)
    description = models.TextField('описание', blank=True)
    image = models.ImageField(
        'картинка',
        blank=True,
        null=True,
        upload_to='media/image/'
    )
    coords = models.JSONField('координаты', blank=True, null=True, default={})

    class Meta:
        verbose_name = 'достопримечательность'
        verbose_name_plural = 'достопримечательности'

    def __str__(self) -> str:
        return self.name
