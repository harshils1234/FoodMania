from django import forms
from django.core.exceptions import ValidationError
from foodmania.models import Category, Food


class CategoryForm(forms.ModelForm):
    """
    This is model form for category model.
    """

    def __init__(self, *args, **kwargs):
        """
        This method will initialise custom class.
        """
        super(CategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Category
        fields = ['name']

    def clean(self):
        """
        This method will validate data from form.
        """
        cleaned_data = super(CategoryForm, self).clean()
        name = self.cleaned_data.get('name')

        if Category.objects.filter(name__iexact=name).exclude(id=self.instance.id).exists():
            raise ValidationError("Category with this name already exists", code='invalid')

        return cleaned_data


class FoodForm(forms.ModelForm):
    """
    This is model form for food model.
    """

    def __init__(self, *args, **kwargs):
        """
        This method will initialise custom class.
        """
        super(FoodForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'select2 form-control'
        self.fields['status'].widget.attrs['class'] = 'select2 form-control'

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Food
        fields = ['name', 'description', 'price', 'image', 'stock', 'category', 'status']
        widgets = {'image': forms.FileInput}

    def clean(self):
        """
        This method will validate data from form.
        """
        cleaned_data = super(FoodForm, self).clean()
        name = self.cleaned_data.get('name')

        if Food.objects.filter(name__iexact=name).exclude(id=self.instance.id).exists():
            raise ValidationError("Food with this name already exists", code='invalid')

        return cleaned_data
