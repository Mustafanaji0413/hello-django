from django.shortcuts import render, redirect
from .models import Item
from .forms import itemForm


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')
    form = itemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)

    def edit_item(request, item_id):
        return render(request, 'todo/edit_item.html')
