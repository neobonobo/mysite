from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import ImportantDate,Todo

def important_date_list(request):
    dates = ImportantDate.objects.all().order_by('-date')
    return render(request, 'chronos/important_date_list.html', {'dates': dates})

def important_date_detail(request, pk):
    date = get_object_or_404(ImportantDate, pk=pk)
    return render(request, 'chronos/important_date_detail.html', {'date': date})

@login_required
def add_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Todo.objects.create(user=request.user, title=title)
    return redirect('home')
