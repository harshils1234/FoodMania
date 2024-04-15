from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    """
    This model will store category details.
    """
    name = models.CharField(max_length=20)

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        verbose_name_plural = 'Categories'

    def __str__(self):
        """
        The method allows us to convert an object into a string representation.
        """
        return self.name


class Food(TimeStampedModel):
    """
    This model will store food details.
    """
    STATUS = (
        ('Disabled', 'Disabled'),
        ('Enabled', 'Enabled')
    )

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="food_images/", default='food_images/default_food.jpg')
    stock = models.IntegerField(default=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='food_items')
    status = models.CharField(max_length=10, choices=STATUS, default='Enabled')

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options, verbose_name, and a lot of other options.
        """
        ordering = ['id']

    def __str__(self):
        """
        The method allows us to convert an object into a string representation.
        """
        return f"Name: {self.name} Price: {self.price} Category: {self.category}"
