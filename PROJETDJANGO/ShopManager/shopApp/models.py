from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='categories' )
    date_add = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nom_categorie


class Produit(models.Model):
    nom_produit = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits')
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_produit}"
          

class PanierClient(models.Model):
    nom_client = models.CharField(max_length=255)
    achat = models.ManyToManyField(Produit, through='Achat')
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_client


class Achat(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='achats')
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Désactivé pour l'utilisateur
    panier = models.ForeignKey(PanierClient, on_delete=models.CASCADE, related_name='achts')
    date_achat = models.DateTimeField(auto_now_add=True)
    mode_payement = models.CharField(max_length=255)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Calculé automatiquement

    def save(self, *args, **kwargs):
        if not self.prix_unitaire:  # Vérifier si le prix_unitaire n'est pas encore défini
            self.prix_unitaire = self.produit.prix  # Récupérer le prix du produit
        
        if self.quantite is not None:
            self.prix_total = self.prix_unitaire * self.quantite  # Calculer le prix total
        
        # Vérifier la quantité disponible
        if self.produit.quantite < self.quantite:
            raise ValueError("Quantité demandée indisponible en stock.") 
        
        # Diminuer la quantité du produit
        self.produit.quantite -= self.quantite
        self.produit.save()  # Sauvegarder la mise à jour du stock
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Achat de {self.quantite} {self.produit.nom_produit} - Total: {self.prix_total} FCFA"


    

    def __str__(self):
        return "Nom Produit :",self.produit.nom_produit, "quantité: ", self.quantite_total, "date achat: ", self.date_achat, "mode payement: ", self.mode_payement

class Facture(models.Model):
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)
    date_facture = models.DateTimeField(auto_now_add=True)
    
