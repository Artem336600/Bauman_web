from django.db import models


class Departments(models.Model):
    title = models.CharField('Кафедра', max_length=50)
    full_text = models.TextField('Предметы')
    date = models.CharField('Часы', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'
