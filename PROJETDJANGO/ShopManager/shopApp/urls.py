from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     #projet : URL menant à la page d'accueil
    path('',views.index, name='index'),

    #projet : URL menant à la page de la liste des produits
    path('liste/', views.listeProduit, name="listeProduit" ),

    #projet : URL menant à la page d'ajout des produits
    path('ajout/', views.ajoutProduit, name = "ajoutProduit")

     #projet : URL menant à la page de la liste des categories
   # path('', views.listeCategorie , name = "listeCategorie"),

  #projet : URL menant à la page d'ajout des categorie
   # path('', views.ajoutCategorie, name = "ajoutCategorie" )
]
