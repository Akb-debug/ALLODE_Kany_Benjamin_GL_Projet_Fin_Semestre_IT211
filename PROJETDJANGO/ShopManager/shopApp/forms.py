from django import forms
from .models import Categorie

class ProduitForm(forms.Form):
    nom_produit = forms.CharField(
        max_length=255,
        label="Nom du produit",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez le nom du produit"}),
    )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Entrez une description"}),
    )
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        label="Catégorie",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    prix = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Prix",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Entrez le prix"}),
    )
    quantite = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Quantité",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Entrez la quantité"}),
    )
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
    )




class CategorieForm(forms.Form):
    nom_categorie = forms.CharField(
        max_length=255,
        label="Nom Categorie",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez la categorie"}),
    )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Entrez une description"}),
        
    )
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
        
    )
  
class  ClientForm(forms.Form):
    nom_client = forms.CharField(
        max_length=255,
        label="Nom Client",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez le nom client"})
    
    )
class AchatForm(forms.Form):
    quantite_total = forms.DecimalField(
        max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    mode_payement = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'})
    )




