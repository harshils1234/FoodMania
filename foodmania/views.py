from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from foodmania.filters import CategoryFilter, FoodFilter
from foodmania.forms import CategoryForm, FoodForm
from foodmania.models import Food, Category
from foodmania_website.forms import AddToCartForm


class CustomPermissionRequired(PermissionRequiredMixin):
    """
    This class will give custom permissions.
    """
    permission_required = ('user.is_staff', 'user.is_superuser')


class CategoryCreateView(LoginRequiredMixin, CustomPermissionRequired, CreateView):
    """
    This class will create category.
    """
    form_class = CategoryForm
    success_url = reverse_lazy('foodmania:category_list')


class CategoryListView(LoginRequiredMixin, CustomPermissionRequired, FilterView):
    """
    This class displays a list of all categories.
    """
    template_name = 'admin/category/category_list.html'
    context_object_name = 'categories'
    filterset_class = CategoryFilter

    def get_queryset(self):
        """
        This method returns a queryset of category model.
        """
        query = self.request.GET.get('search')
        if query:
            return Category.objects.filter(
                Q(name__icontains=query))
        return Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        This method will pass extra context to template.
        """
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['form'] = CategoryForm
        return context


class CategoryUpdateView(LoginRequiredMixin, CustomPermissionRequired, UpdateView):
    """
    This class will update category.
    """
    model = Category
    form_class = CategoryForm
    template_name = 'admin/category/category_create.html'
    success_url = reverse_lazy('foodmania:category_list')


class CategoryDeleteView(LoginRequiredMixin, CustomPermissionRequired, DeleteView):
    """
    This class will delete category.
    """
    model = Category
    success_url = reverse_lazy('foodmania:category_list')

    def post(self, request, *args, **kwargs):
        category = get_object_or_404(Category, pk=kwargs['pk'])
        category.delete()
        return JsonResponse({'success': True})


class FoodCreateView(LoginRequiredMixin, CustomPermissionRequired, CreateView):
    """
    This food will create food.
    """
    form_class = FoodForm
    success_url = reverse_lazy('foodmania:food_list')


class FoodListView(LoginRequiredMixin, FilterView):
    """
    This class displays a list of all food items.
    """
    template_name = 'admin/food/food_list.html'
    context_object_name = 'items'
    filterset_class = FoodFilter
    paginate_by = 6

    def get_queryset(self):
        """
        This method returns a queryset of food model.
        """
        query = self.request.GET.get('search')

        if query:
            return Food.objects.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query))
        elif "popularity" in self.request.GET:
            return Food.objects.order_by('created')
        elif "price_low_to_high" in self.request.GET:
            return Food.objects.order_by('price')
        elif "price_high_to_low" in self.request.GET:
            return Food.objects.order_by('-price')
        else:
            return Food.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        This method will pass extra context to template.
        """
        context = super(FoodListView, self).get_context_data(**kwargs)
        context['form'] = FoodForm
        context['add_to_cart'] = AddToCartForm
        return context


class FoodUpdateView(LoginRequiredMixin, CustomPermissionRequired, UpdateView):
    """
    This class will update food.
    """
    model = Food
    form_class = FoodForm
    template_name = 'admin/food/food_create.html'
    success_url = reverse_lazy('foodmania:food_list')


class FoodDeleteView(LoginRequiredMixin, CustomPermissionRequired, DeleteView):
    """
    This class will delete food.
    """
    model = Food
    success_url = reverse_lazy('foodmania:food_list')
