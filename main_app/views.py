from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Crystal, Collection
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
  id_list = crystal.collections.all().values_list('id')
  not_in_collection = Collection.objects.exclude(id__in=id_list)
  reading_form = ReadingForm()
  return render(request, 'crystals/detail.html', 
                {
                'crystal': crystal, 
                'reading_form': reading_form,
                'collections': not_in_collection
                })
                
def assoc_collection(request, crystal_id, collection_id):
  Crystal.objects.get(id=crystal_id).collections.add(collection_id)
  return redirect('detail', crystal_id=crystal_id)

def remove_assoc_collection(request, crystal_id, collection_id):
  Crystal.objects.get(id=crystal_id).collections.remove(collection_id)
  return redirect('detail', crystal_id=crystal_id )

def add_reading(request, crystal_id):
    form = ReadingForm(request.POST)
    if form.is_valid():
     new_reading = form.save(commit=False)
     new_reading.crystal_id = crystal_id
     new_reading.save()
    return redirect('detail', crystal_id=crystal_id)
  
class CrystalCreate(CreateView):
  model = Crystal
  fields = ['name', 'color', 'properties', 'image', 'zodiac']

class CrystalUpdate(UpdateView):
  model = Crystal
  fields = ['color', 'properties', 'image', 'zodiac']

class CrystalDelete(DeleteView):
  model = Crystal
  success_url = '/crystals'

class CollectionList(ListView):
  model = Collection

class CollectionDetail(DetailView):
  model = Collection

class CollectionCreate(CreateView):
  model = Collection
  fields = '__all__'

class CollectionUpdate(UpdateView):
  model = Collection
  fields = ['name', 'image']

class CollectionDelete(DeleteView):
  model = Collection
  success_url = '/collections'
  