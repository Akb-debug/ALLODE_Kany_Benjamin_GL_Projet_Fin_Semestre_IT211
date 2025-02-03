from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='categories' )
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.nom_categorie


class Produit(models.Model):
    nom_produit = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits')
    date_add = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return "Nom produit :", self.nom_produit, "categorie :", self.categorie.nom_categorie, "prix Unitaire: ", self.prix, "quantité: ", self.quantite


class PanierClient(models.Model):
    nom_client = models.CharField(max_length=255)
    achat = models.ManyToManyField(Produit, through='Achat')
    date_add = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nom_client

class Achat(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='achats')
    quantite_total = models.DecimalField(max_digits=10, decimal_places=2)
    panier = models.ForeignKey(PanierClient, on_delete=models.CASCADE, related_name='achts')
    date_achat = models.DateTimeField(auto_now_add=True)
    mode_payement = models.CharField(max_length=255)

    def _str_(self):
        return "Nom Produit :",self.produit.nom_produit, "quantité: ", self.quantite_total, "date achat: ", self.date_achat, "mode payement: ", self.mode_payement

class Facture(models.Model):
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)
    date_facture = models.DateTimeField(auto_now_add=True)
    
