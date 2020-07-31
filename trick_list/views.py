from django.shortcuts import render, get_object_or_404, redirect
from .models import To_learn
from .forms import TrickForm, LearnForm
from django.http import HttpResponseRedirect



# Create your views here.

def home(request):
	form = TrickForm()
	li = To_learn.objects.all()
	if request.method == 'POST':
		form = TrickForm(request.POST)
		if form.is_valid():
			form.save()
			form = TrickForm()
	context = {
		'form': form,
		'li': li
	}
	return render(request, 'trick_list/home.html', context)


def trick_delete(request, id):
	obj = get_object_or_404(To_learn, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('/home/')
	context = {
		'object': obj
	}
	return render(request, 'trick_list/home.html', context)


def trick_view(request, id):
	trick_name = To_learn.objects.get(pk=id)
	learn = LearnForm()
	if request.method == 'POST':
		learn = LearnForm(request.POST, instance=trick_name)
		if learn.is_valid():
			learn.save()
			return redirect('trick_list:trick_view', id=trick_name.id)
	context = {
		'id': id,
		'trick_name': trick_name,
		'learn': learn
	}
	return render(request, 'trick_list/trick.html', context)	


def category_view(request, cat):
	trick_category = To_learn.objects.filter(category=cat )
	context = {
		'cat': cat,
		'trick_category': trick_category
	}
	return render(request, 'trick_list/categories.html', context)

