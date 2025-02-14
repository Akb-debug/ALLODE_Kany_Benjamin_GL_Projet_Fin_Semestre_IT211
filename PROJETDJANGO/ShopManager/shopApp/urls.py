from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     #projet : URL menant à la page d'accueil
    path('',views.index, name='index'),

    #projet : URL menant à la page de la liste des produits
    path('listeProduit/', views.listeProduit, name="listeProduit" ),

    #projet : URL menant à la page de la liste des produits
    path('listeProduit2/', views.listeProduit2, name="listeProduit2" ),

    #projet : URL menant à la page d'ajout des produits
    path('ajoutProduit/', views.ajoutProduit, name = "ajoutProduit"),


    
    #projet : URL menant à la page d'ajout des produits
    path('ajoutClient/', views.ajoutClient, name = "ajoutClient"),


     #projet : URL menant à la page de la liste des categories
    path('listeCategorie/', views.listeCategorie , name = "listeCategorie"),

  #projet : URL menant à la page d'ajout des categorie
    path('ajoutCategorie/', views.ajoutCategorie, name = "ajoutCategorie" ),

     #projet : URL menant à la page de la liste des achats
    path('listeAchat/', views.listeAchat , name = "listeAchat"),

     #projet : URL menant à la page de la liste des categories
    path('listeClient/', views.listeClient, name = "listeClient"),

     #projet : URL menant à la page de la liste des categories
    path('listeFacture/', views.listeFacture , name = "listeFacture"),


    #Supprimer produit
        path('produit/supprimerProduit/<int:produit_id>/', views.supprimerProduit, name='supprimerProduit'),

         #Supprimer categorie
        path('categorie/supprimercategorie/<int:categorie_id>/', views.supprimerCategorie, name='supprimerCategorie'),

        #Modiier Prduit
        path('produit/modifierProduit/<int:produit_id>/', views.modifierProduit, name='modifierProduit'),

        #Modifier categorie
        path('categorie/modifierCategorie/<int:categorie_id>/', views.modifierCategorie, name='modifierCategorie'),

        # Ajout Achat
        path('ajoutAchat/<int:produit_id>/', views.ajoutAchat, name='ajoutAchat'),


  ]
