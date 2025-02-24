from django.shortcuts import render , redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from shopApp.models import *
from .forms import *
from django.db.models import Sum, Count
from django.utils import timezone


# Create your views here.

    
#projet/: URL menant à la page d'accueil 
#Methode d'affichage du menu

def index(request):
    # Récupération des produits ayant été achetés au moins une fois
    produits = Produit.objects.annotate(total_vendu=Sum('achats__quantite')).filter(total_vendu__gt=0).order_by('-total_vendu')[:3]
    total1 = Categorie.objects.count()
    total2 = Produit.objects.count()
    total3 = Achat.objects.count()
    total4 = PanierClient.objects.count()
    argent = Produit.objects.aggregate(argent=Sum('achats__prix_total'))['argent'] or 0
    #Recuperer les données pour le  graphe
    ventes = Achat.objects.filter(date_achat__isnull=False)
    date_ventes = [vente.date_achat.strftime("%y/%m/%d") for vente in ventes]
    chiffre_ventes = [vente.prix_total for vente in ventes]
    contexte = {'produits': produits,'total1':total1,'total2':total2,'total3':total3,'total4':total4,'argent':argent,'date_ventes':date_ventes,'chiffre_ventes':chiffre_ventes }
    return render(request, 'projet/index.html', contexte)

#projet/: URL menant à la page de la liste des produits
#Methode d'affichage de la liste des produits
def listeProduit(request):
    if request.method == "POST":
        nom = request.POST.get("produit")
        nom_categorie = request.POST.get("categorie")
        
        produits = Produit.objects.all()

        if nom:
            
            produits = produits.filter(nom_produit__icontains=nom)
        if nom_categorie:
            categories = Categorie.objects.all()
            categories = categories.filter(nom_categorie__icontains = nom_categorie)
            produits = produits.filter(categorie__in = categories)

        context = {"listeProduit": produits}
        return render(request, "projet/listeProduit.html", context)

    else:
        produits = Produit.objects.all().order_by('id')
        context = {"listeProduit": produits}
        return render(request, "projet/listeProduit.html", context)



#Liste produit
def listeProduit2(request):
    produits = Produit.objects.all().order_by('id')
    context = {"listeProduit": produits}
    return render(request , "projet/listeProduit2.html", context) 
    

#Liste Client
def listeClient(request):
    clients = PanierClient.objects.all()
    context = {"listeClient": clients}
    return render(request , "projet/listeClient.html", context) 

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
        categorieform = CategorieForm(request.POST, request.FILES)
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
        categorieform = CategorieForm()
        
    return render(request , "projet/ajoutCategorie.html", {"categorieForm":categorieform})

#Liste achat
def listeAchat(request):
    achats = Achat.objects.all()
    contexte = {'listeAchat':achats}
    return render(request , "projet/listAchat.html", contexte)


def listeClient(request):
    clients = PanierClient.objects.all()
    contexte = {'listeClient':clients}
    return render(request , "projet/listeClient.html",contexte)   


def listeFacture(request):
    clients = PanierClient.objects.all()
    contexte = {'listeClient':clients}
    return render(request , "projet/listeFacture.html",contexte)   
       
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


# Modifier categorie
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

def ajoutClient(request):
#Requête POST 
    if request.method == "POST":
        #1 Récuperer les données
        clientform = ClientForm(request.POST)
        #2 Valider les données
        if clientform.is_valid():
            #3 Preparation des données 
            nom =clientform.cleaned_data["nom_client"]
            #4 Création et sauvegarde d'un produit
            oClient  = PanierClient(nom_client =nom)
            oClient.save()
            #5 Rediriger vers page listeProduit
            return redirect("listeProduit2")
    else:
        #Formulaire vide pour requête GET 
        clientform = ClientForm()
        
    return render(request , "projet/ajouterClient.html", {"clientForm":clientform})




def ajoutAchat(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    panier = PanierClient.objects.order_by('-id').first()


    if request.method == "POST":
        try:
            achatform = AchatForm(request.POST)
            if achatform.is_valid():
                quantite = achatform.cleaned_data['quantite_total']
                mode_payement = achatform.cleaned_data['mode_payement']

            if quantite <= 0:
                messages.error(request, "La quantité doit être supérieure à zéro.")
                return redirect("ajoutAchat", produit.id)  

            # Vérifier si la quantité demandée est disponible
            if produit.quantite < quantite:
                messages.error(request, "Stock insuffisant pour cet article.")
                return redirect("ajoutAchat", produit.id)   
            
                # Enregistrement manuel dans la base de données
            oAchat  = Achat(produit = produit,quantite=quantite,panier=panier,mode_payement=mode_payement)
            oAchat.save()

            messages.success(request, "Produit ajouté au panier avec succès !")
            return redirect('listeProduit2')  


        except Produit.DoesNotExist:
            messages.error(request, "Produit introuvable.")
        except ValueError:
            messages.error(request, "Quantité invalide.")
        except Exception as e:
            messages.error(request, f"Erreur : {str(e)}")

            #return redirect('listeProduit2')  
    else:
       achatform = AchatForm()
    return render(request , "projet/ajoutAchat.html", {"achatForm":achatform,"produit": produit})


#Supprimer achat
def supprimerAchat(request, achat_id):
    # Récupérer l'élément ou lever une erreur 404 s'il n'existe pas
    oAchat = get_object_or_404(Achat, id=achat_id)
    
    # Supprimer l'élément
    oAchat.delete()
    
    # Rediriger vers une autre page après la suppression 
    return redirect('listeAchat') 


#Sppression client
def supprimerClient(request, panier_id):
    # Récupérer l'élément ou lever une erreur 404 s'il n'existe pas
    panier = get_object_or_404(PanierClient, id=panier_id)
    
    # Supprimer l'élément
    panier.delete()
    
    # Rediriger vers une autre page après la suppression 
    return redirect('listeClient')  



def dtailPanier(request, panier_id):
    opanier = get_object_or_404(PanierClient, id=panier_id)

    achat = Achat.objects.filter(panier=opanier)

    context = {"listeAchat": achat}
    return render(request, "projet/listeAchatPanier.html", context)


def imprimerFacture(request, panier_id):
    opanier = get_object_or_404(PanierClient, id=panier_id)

    listeAchat = Achat.objects.filter(panier=opanier)
    total = sum(a.prix_total for a in listeAchat) 
    context = {"listeAchat": listeAchat, 'total': total}
    return render(request, "projet/imprimerFacture.html", context)


# Modifier client
def modifierClient(request, client_id):
    # Récupérer l'élément ou lever une erreur 404
    client = get_object_or_404(PanierClient, id=client_id)

    if request.method == "POST":
        # Récupérer les données du formulaire soumis
        clientform = ClientForm(request.POST)
        if clientform.is_valid():
            # Mettre à jour les données du client
            client.nom_client = clientform.cleaned_data["nom_client"]

            # Sauvegarder le produit
            client.save()
            return redirect("listeClient")
    else:
        # Pré-remplir le formulaire avec les données existantes
        initial_data = {
            'nom_client': client.nom_client,
        }
        clientform = ClientForm(initial=initial_data)

    return render(request, "projet/modifierClient.html", {"clientForm": clientform, 'client':client})




# Modifier achat
def modifierAchat(request, achat_id):
    # Récupérer l'élément ou lever une erreur 404
    achat = get_object_or_404(Achat, id=achat_id)

    if request.method == "POST":
        # Récupérer les données du formulaire
        achatform = AchatForm(request.POST)
        if achatform.is_valid():
            # Mettre à jour les données du produit
            achat.quantite = achatform.cleaned_data["quantite_total"]
            achat.mode_payement = achatform.cleaned_data["mode_payement"]
            

            # Sauvegarder l'achat
            achat.save()
            return redirect("listeAchat")
    else:
        # Pré-remplir le formulaire avec les données existantes
        initial_data = {
            'quantite_total': achat.quantite,
            'mode_payement': achat.mode_payement, 
        }
        achatform = AchatForm(initial=initial_data)

        return render(request, "projet/modifierAchat.html", {"achatForm": achatform, "achat": achat})