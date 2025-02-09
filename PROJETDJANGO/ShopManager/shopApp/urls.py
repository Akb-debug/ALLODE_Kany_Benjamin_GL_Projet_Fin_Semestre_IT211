from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     #projet : URL menant à la page d'accueil
    path('',views.index, name='index'),

    #projet : URL menant à la page de la liste des produits
    path('liste1/', views.listeProduit, name="listeProduit" ),

    #projet : URL menant à la page d'ajout des produits
    path('ajout1/', views.ajoutProduit, name = "ajoutProduit"),

     #projet : URL menant à la page de la liste des categories
    path('liste2/', views.listeCategorie , name = "listeCategorie"),

  #projet : URL menant à la page d'ajout des categorie
    path('ajout2/', views.ajoutCategorie, name = "ajoutCategorie" ),

     #projet : URL menant à la page de la liste des achats
    path('liste3/', views.listeAchat , name = "listeAchat"),

     #projet : URL menant à la page de la liste des categories
    path('liste4/', views.listeClient, name = "listeClient"),

     #projet : URL menant à la page de la liste des categories
    path('liste2/', views.listeFacture , name = "listeFacture"),


    #Supprimer produit
        path('produit/supprimer/<int:produit_id>/', views.supprimerProduit, name='supprimerProduit'),
        path('categorie/supprimer/<int:categorie_id>/', views.supprimerCategorie, name='supprimerCategorie'),
        path('categorie/modifierProduit/<int:produit_id>/', views.modifierProduit, name='modifierProduit'),
  ]
