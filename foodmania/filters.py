import django_filters
from django import forms
from .models import Category, Food


class CategoryFilter(django_filters.FilterSet):
    """
    This is filter class for category model.
    """
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}))

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Category
        fields = ['name']


class FoodFilter(django_filters.FilterSet):
    """
    This is filter class for food model.
    """
    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}))
    status = django_filters.ChoiceFilter(choices=Food.STATUS,
                                         widget=forms.RadioSelect(attrs={'class': 'radio'}))

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Food
        fields = ['category', 'status']
