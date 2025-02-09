from django import forms
from .models import Categorie

class ProduitForm(forms.Form):
    nom_produit = forms.CharField(
        max_length=255,
        label="Nom du produit",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez le nom du produit"}),
        error_messages={"required": ""}  # Message personnalisé vide
    )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Entrez une description"}),
        error_messages={"required": ""}  # Message personnalisé vide
    )
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        label="Catégorie",
        widget=forms.Select(attrs={"class": "form-select"}),
        error_messages={"required": ""}  # Message personnalisé vide
    )
    prix = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Prix",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Entrez le prix"}),
        error_messages={"required": ""}  # Message personnalisé vide
    )
    quantite = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Quantité",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Entrez la quantité"}),
        error_messages={"required": ""}  # Message personnalisé vide
    )
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
        error_messages={"required":""}  # Message personnalisé vide
    )




class categorieForm(forms.Form):
    nom_categorie = forms.CharField(
        max_length=255,
        label="Nom Categorie",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez la categorie"}),
        error_messages={"required": ""}  # Message personnalisé vide
    )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Entrez une description"}),
        error_messages={"required": ""}  # Message personnalisé vide
    )
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
        error_messages={"required":""}  # Message personnalisé vide
    )
   