from django.db import models


class Category(models.Model):
    name = models.CharField(
        'Category name',
        max_length=250,
    )

    @property
    def info(self):
        return f'{self.name}'


class Recipes(models.Model):
    title = models.CharField(
        'Title',
        max_length=250,
    )
    description = models.TextField(
        'Description'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL
    )

    @property
    def full_info(self):
        return f'{self.title}, {self.description}, {self.category}'

    def short_info(self):
        return f'{self.title} {self.category}'

    def __str__(self):
        return self.full_info

    class Meta:
        ordering = ['title', 'category']
        indexes = [
            models.Index(fields=['title', 'category']),
        ]