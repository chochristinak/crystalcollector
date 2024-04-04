from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  
  path('about/', views.about, name='about'),

  path('crystals/', views.crystals_index, name='index'),

  path('crystals/<int:crystal_id>/', views.crystals_detail, name='detail'),

  path('crystals/create', views.CrystalCreate.as_view(), name='crystals_create'),

  path('crystals/<int:crystal_id>/add_reading/', views.add_reading, name='add_reading'),

  path('crystals/<int:crystal_id>/assoc_collection/<int:collection_id>/', views.assoc_collection, name='assoc_collection'),
  path('crystals/<int:crystal_id>/remove_assoc_collection/<int:collection_id>/', views.remove_assoc_collection, name='remove_assoc_collection'),


  path('crystals/<int:pk>/update/', views.CrystalUpdate.as_view(), name='crystals_update'),

  path('crystals/<int:pk>/delete/', views.CrystalDelete.as_view(), name='crystals_delete'),



  path('collections/', views.CollectionList.as_view(), name='collections_index'),
  path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collections_detail'),
  path('collections/create/', views.CollectionCreate.as_view(), name='collections_create'),
  path('collections/<int:pk>/update/', views.CollectionUpdate.as_view(), name='collections_update'),
  path('collections/<int:pk>/delete/', views.CollectionDelete.as_view(), name='collections_delete'),

]