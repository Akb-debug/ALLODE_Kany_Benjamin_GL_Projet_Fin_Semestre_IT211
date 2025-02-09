from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from shopApp.models import *
from .forms import *


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



#projet/: URL menant à la page de la liste des categories
#Methode d'affichage de la liste des categorie
def listeCategorie(request):
    context = {"listeCategorie":Categorie.objects.all() }
    return render(request , "projet/listeCategorie.html", context) 


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
    



def ajoutCategorie(request):
#Requête POST 
    if request.method == "POST":
        #1 Récuperer les données
        categorieform = categorieForm(request.POST, request.FILES)
        #2 Valider les données
        if categorieform.is_valid():
            #3 Preparation des données 
            nom =categorieform.cleaned_data["nom_categorie"]
            desc = categorieform.cleaned_data["description"]
            imge =categorieform.cleaned_data["image"]
            #4 Création et sauvegarde d'un produit
            oCategorie  = Categorie(nom_categorie =nom , description = desc, image =imge)
            oCategorie.save()
            #5 Rediriger vers page listeProduit
            return redirect("listeCategorie")
    else:
        #Formulaire vide pour requête GET 
        categorieform = categorieForm()
        
    return render(request , "projet/ajoutCategorie.html", {"categorieForm":categorieform})

def listeAchat(request):
    return render(request , "projet/listAchat.html")


def listeFacture(request):
    return render(request , "projet/listFacture.html")


def listeClient(request):
    return render(request , "projet/listFacture.html")      
#Sppression produit
def supprimerProduit(request, produit_id):
    # Récupérer l'élément ou lever une erreur 404 s'il n'existe pas
    produit = get_object_or_404(Produit, id=produit_id)
    
    # Supprimer l'élément
    produit.delete()
    
    # Rediriger vers une autre page après la suppression 
    return redirect('listeProduit')  

#Modification produit

def modifierProduit(request, produit_id):
    # Récupérer l'élément ou lever une erreur 404
    produit = get_object_or_404(Produit, id=produit_id)

    if request.method == "POST":
        # Récupérer les données du formulaire soumis
        produitform = ProduitForm(request.POST, request.FILES)
        if produitform.is_valid():
            # Mettre à jour les données du produit
            produit.nom_produit = produitform.cleaned_data["nom_produit"]
            produit.description = produitform.cleaned_data["description"]
            produit.categorie = produitform.cleaned_data["categorie"]
            produit.prix = produitform.cleaned_data["prix"]
            produit.quantite = produitform.cleaned_data["quantite"]
            produit.image = produitform.cleaned_data["image"]

            # Sauvegarder le produit
            produit.save()
            return redirect("listeProduit")
    else:
        # Pré-remplir le formulaire avec les données existantes
        initial_data = {
            'nom_produit': produit.nom_produit,
            'description': produit.description,
            'categorie': produit.categorie,
            'prix': produit.prix,
            'quantite': produit.quantite,
            'image': produit.image,
        }
        produitform = ProduitForm(initial=initial_data)

    return render(request, "projet/modifierProduit.html", {"produitForm": produitform, 'produit': produit})


       
       
       
       
        #Supprimer categorie
def supprimerCategorie(request, categorie_id):
    # Récupérer l'élément ou lever une erreur 404 s'il n'existe pas
    ocategorie = get_object_or_404(Categorie, id=categorie_id)
    
    # Supprimer l'élément
    ocategorie.delete()
    
    # Rediriger vers une autre page après la suppression 
    return redirect('listeCategorie')  



def modifierCategorie(request, categorie_id):
    # Récupérer l'élément ou lever une erreur 404
    categorie = get_object_or_404(Categorie, id=categorie_id)

    if request.method == "POST":
        # Récupérer les données du formulaire soumis
        categorieform = CategorieForm(request.POST, request.FILES)
        if categorieform.is_valid():
            # Mettre à jour les données du produit
            categorie.nom_categorie = categorieform.cleaned_data["nom_categorie"]
            categorie.description = categorieform.cleaned_data["description"]
            categorie.image = categorieform.cleaned_data["image"]



 
            # Sauvegarder le produit
            categorie.save()
            return redirect("listeCategorie")
    else:
        # Pré-remplir le formulaire avec les données existantes
        initial_data = {
            'nom_categorie': categorie.nom_categorie,
            'description': categorie.description,
            'image': categorie.image,
        }
        categorieform = CategorieForm(initial=initial_data)

    return render(request, "projet/modifierCategorie.html", {"categorieForm": categorieform, 'categorie':categorie})



