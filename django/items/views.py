from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def home(request):
    items = Item.objects.all()
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'home.html', {'items': items, 'form': form})

