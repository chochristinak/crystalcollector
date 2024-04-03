from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Crystal
from .forms import ReadingForm



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def crystals_index(request):
  crystals = Crystal.objects.all()
  return render(request, 'crystals/index.html',
                 {
                   'crystals': crystals
                   })
def crystals_detail(request, crystal_id):
  crystal = Crystal.objects.get(id=crystal_id)
  reading_form = ReadingForm()
  return render(request, 'crystals/detail.html', 
                {
                'crystal': crystal, 'reading_form': reading_form
                })

def add_reading(request, crystal_id):
    form = ReadingForm(request.POST)
    if form.is_valid():
     new_reading = form.save(commit=False)
     new_reading.crystal_id = crystal_id
     new_reading.save()
    return redirect('detail', crystal_id=crystal_id)
  
class CrystalCreate(CreateView):
  model = Crystal
  fields = '__all__'

class CrystalUpdate(UpdateView):
  model = Crystal
  fields = ['color', 'properties', 'shakra', 'mohs', 'image']

class CrystalDelete(DeleteView):
  model = Crystal
  success_url = '/crystals'
  