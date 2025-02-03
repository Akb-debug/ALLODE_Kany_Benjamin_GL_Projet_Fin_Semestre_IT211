from django.shortcuts import render , redirect
from django.http import HttpResponse
from shopApp.models import *
from .forms import ProduitForm

# Create your views here.

#projet/: URL menant à la page d'accueil 
#Methode d'affichage du menu
def index(request):
    return render(request, 'projet/index.html')

#projet/: URL menant à la page de la liste des produits
#Methode d'affichage de la liste des produits
def listeProduit(request):
    context = {"listeProduit":Produit.objects.all() }
    return render(request , "projet/listeProduit.html", context) 

#projet/: URL menant à la page d'ajout des produits
#Methode d'ajout des produits
def ajoutProduit(request):
    #Requête POST 
    if request.method == "POST":
        #1 Récuperer les données
        produitform = ProduitForm(request.POST, request.FILES)
        #2 Valider les données
        if produitform.is_valid():
            #3 Preparation des données 
            nom = produitform.cleaned_data["nom_produit"]
            desc = produitform.cleaned_data["description"]
            cat = produitform.cleaned_data["categorie"]
            pu = produitform.cleaned_data["prix"]
            qt = produitform.cleaned_data["quantite"]
            imge = produitform.cleaned_data["image"]
            #4 Création et sauvegarde d'un produit
            oProduit1  = Produit(nom_produit =nom , description = desc, categorie = cat, prix = pu, quantite=qt, image =imge)
            oProduit1.save()
            #5 Rediriger vers page listeProduit
            return redirect("listeProduit")
    else:
        #Formulaire vide pour requête GET 
        produitform = ProduitForm()
        
    return render(request , "projet/ajoutProduit.html", {"produitForm":produitform})
    