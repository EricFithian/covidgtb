from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, Vaccine, Vaccinating
from django.views import View

#Here are my class based views

class TestListView(View):
    def get(self, request):
        queryset = Test.objects.all()
        context = {
            'objects': queryset
        }
        return render(request, 'tests/test_list.html', context)

class VaccineListView(View):
    def get(self, request):
        queryset = Vaccine.objects.all()
        context = {
            'objects': queryset
        }
        return render(request, 'vaccines/vaccine_list.html', context)

class VaccinationsListView(View):
    def get(self, request):
        queryset = Vaccinating.objects.all()
        context = {
            'objects': queryset
        }
        return render(request, 'vaccinations/vaccinations_list.html', context)

# Create your function views here.

def home(request):
    return render(request, 'home.html')

def symptoms(request):
    return render(request, 'symptoms.html')

def testing_lookup(request, id):
    obj = get_object_or_404(Test, id=id)
    context = {
        'object': obj
    }
    return render(request, 'tests/test_detail.html', context)

def testing_delete(request, id):
    obj = get_object_or_404(Test, id=id)
    if request.method == "POST":
        #Building this in to make sure they don't delete just by going
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, 'tests/test_delete.html', context)

def vaccines_lookup(request, id):
    obj = get_object_or_404(Vaccine, id=id)
    context = {
        'object': obj
    }
    return render(request, 'vaccines/vaccine_detail.html', context)

def vaccines_delete(request, id):
    obj = get_object_or_404(Vaccine, id=id)
    if request.method == "POST":
        #Building this in to make sure they don't delete just by going
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, 'vaccines/vaccine_delete.html', context)

def vaccinations_lookup(request, id):
    obj = get_object_or_404(Vaccinating, id=id)
    context = {
        'object': obj
    }
    return render(request, 'vaccinations/vaccinations_detail.html', context)

def vaccinations_delete(request, id):
    obj = get_object_or_404(Vaccinating, id=id)
    if request.method == "POST":
        #Building this in to make sure they don't delete just by going
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, 'vaccinations/vaccinations_delete.html', context)