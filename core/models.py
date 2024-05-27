from django.db import models


class Attractions(models.Model):
    name = models.CharField('название', max_length=255)
    description = models.TextField('описание', blank=True)
    latitude = models.DecimalField('широта', max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField('долгота', max_digits=10, decimal_places=7, null=True, blank=True)
    categories = models.ForeignKey(
        'Category',
        verbose_name='категории',
        related_name='attractions',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'достопримечательность'
        verbose_name_plural = 'достопримечательности'

    def __str__(self) -> str:
        return self.name


class AttractionImage(models.Model):
    attraction = models.ForeignKey(
        Attractions,
        verbose_name='достопримечательности',
        on_delete=models.CASCADE,
        related_name='attraction_images'
    )
    image = models.ImageField(
        'картинка',
        blank=True,
        null=True,
        upload_to='image/'
    )

    class Meta:
        verbose_name = 'картинка достопримечательности'
        verbose_name_plural = 'картинки достопримечательностей'


class Category(models.Model):
    name = models.CharField('название', max_length=255)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name
