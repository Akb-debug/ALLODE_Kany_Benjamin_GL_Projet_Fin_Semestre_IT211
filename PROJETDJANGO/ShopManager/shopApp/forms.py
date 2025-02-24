from django import forms
from .models import Categorie

class ProduitForm(forms.Form):
    nom_produit = forms.CharField(
        max_length=255,
        label="Nom du produit",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez le nom du produit","pattern": "^[A-Za-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ0-9 ]*$",  # Accepte les lettres en premier
            "title": "Le premier caractère doit être une lettre et le champ ne peut pas contenir uniquement des chiffres."}),
    )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Entrez une description","style":"height:5px"}),
    )
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        label="Catégorie",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    prix = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
         min_value=0,
        label="Prix",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Entrez le prix","title": "Le prix doit être supérieur à 0."}),
    )
    quantite = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0,
        label="Quantité",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Entrez la quantité","title": "La quantité doit être supérieur à 0."}),
    )
    image = forms.ImageField(
        label="Image",
        required= False,
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
    )




class CategorieForm(forms.Form):
    nom_categorie = forms.CharField(
        max_length=255,
        label="Nom Categorie",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez la categorie","pattern": "^[A-Za-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ0-9 ]*$"}),
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
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez le nom client","pattern": "^[A-Za-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ0-9 ]*$"})
    
    )
class AchatForm(forms.Form):
    quantite_total = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    mode_payement = forms.ChoiceField(  # Utilisation correcte d'un champ de choix
        choices=[
            ('Espèces', 'Espèces'),
            ('carte Bancaire', 'Carte Bancaire'),
            ('tmoney', 'tmoney'),
             ('Flooz', 'Flooz')
        ],
        widget=forms.Select(attrs={"class": "form-select"})
    )


