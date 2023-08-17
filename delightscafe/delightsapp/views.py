from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ingredient, RecipeRequirement, Purchase, MenuItem
from django.db.models import Sum
from django.db import models
from .forms import IngredientCreateForm, MenuItemCreateForm, IngredientUpdateForm, MenuItemUpdateForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout


class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "delightsapp/ingredients.html"
    context_object_name = "ingredient_list"


class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "delightsapp/purchases.html"
    context_object_name = "purchase_list"


class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "delightsapp/menu.html"
    context_object_name = "menu_items"


@staff_member_required
def show_balance(request):
    purchased_amount = Purchase.objects.aggregate(total=Sum ("menu_item__price_per_entry"))["total"]
    costs = RecipeRequirement.objects.aggregate(total=Sum("ingredient__price_per_unit", output_field=models.FloatField())
                                                      * Sum("quantity"))["total"]

    profit = purchased_amount - costs

    context = {
        "purchased_amount": purchased_amount,
        "costs": costs,
        "profit": profit,
        }

    return render(request, "delightsapp/balance.html", context)


class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = "delightsapp/ingredient_create.html"


class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientUpdateForm
    template_name = "delightsapp/ingredient_update.html"


class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "delightsapp/ingredient_delete.html"
    success_url = "/ingredients"


class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    template_name = "delightsapp/menu_create.html"


class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    form_class = MenuItemUpdateForm
    template_name = "delightsapp/menu_update.html"


class MenuItemDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "delightsapp/menu_delete.html"
    success_url = "/menu"


def menu_view(request):
    menu_items = MenuItem.objects.all()
    context = {'menu_items': menu_items}
    return render(request, "delightsapp/home.html", context)


def login_view(request):
    context = {
        "login_view": "active"
        }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Add your code below:
        user = authenticate(request, username=username, password=password)

        if user is not None:
            return redirect("home")
        else:
            return HttpResponse("invalid credentials")
    return render(request, "delightsapp/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")