import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Pizzeria,
    R_le,
    Produit,
    Recette,
    Cat_gorie,
    Ingr_dient,
    Stock,
    Livraison,
    Adresse,
    Etat,
    Commande,
    Class,
    Utilisateur,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pizzeria_is_not_abstract():
    assert not inspect.isabstract(Pizzeria)


def test_pizzeria_constructor_exists():
    assert callable(Pizzeria.__init__)


def test_pizzeria_constructor_args():
    sig = inspect.signature(Pizzeria.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "id" in params, "Missing parameter 'id'"
    assert "adresse_id" in params, "Missing parameter 'adresse_id'"

def test_pizzeria_has_nom():
    assert hasattr(Pizzeria, "nom")
    descriptor = None
    for klass in Pizzeria.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_pizzeria_has_id():
    assert hasattr(Pizzeria, "id")
    descriptor = None
    for klass in Pizzeria.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pizzeria_has_adresse_id():
    assert hasattr(Pizzeria, "adresse_id")
    descriptor = None
    for klass in Pizzeria.__mro__:
        if "adresse_id" in klass.__dict__:
            descriptor = klass.__dict__["adresse_id"]
            break
    assert isinstance(descriptor, property)



def test_r_le_is_not_abstract():
    assert not inspect.isabstract(R_le)


def test_r_le_constructor_exists():
    assert callable(R_le.__init__)


def test_r_le_constructor_args():
    sig = inspect.signature(R_le.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_r_le_has_type():
    assert hasattr(R_le, "type")
    descriptor = None
    for klass in R_le.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_r_le_has_id():
    assert hasattr(R_le, "id")
    descriptor = None
    for klass in R_le.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_produit_is_not_abstract():
    assert not inspect.isabstract(Produit)


def test_produit_constructor_exists():
    assert callable(Produit.__init__)


def test_produit_constructor_args():
    sig = inspect.signature(Produit.__init__)
    params = list(sig.parameters.keys())
    assert "categorie_id" in params, "Missing parameter 'categorie_id'"
    assert "id" in params, "Missing parameter 'id'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "prix" in params, "Missing parameter 'prix'"

def test_produit_has_categorie_id():
    assert hasattr(Produit, "categorie_id")
    descriptor = None
    for klass in Produit.__mro__:
        if "categorie_id" in klass.__dict__:
            descriptor = klass.__dict__["categorie_id"]
            break
    assert isinstance(descriptor, property)

def test_produit_has_id():
    assert hasattr(Produit, "id")
    descriptor = None
    for klass in Produit.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_produit_has_nom():
    assert hasattr(Produit, "nom")
    descriptor = None
    for klass in Produit.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_produit_has_prix():
    assert hasattr(Produit, "prix")
    descriptor = None
    for klass in Produit.__mro__:
        if "prix" in klass.__dict__:
            descriptor = klass.__dict__["prix"]
            break
    assert isinstance(descriptor, property)



def test_recette_is_not_abstract():
    assert not inspect.isabstract(Recette)


def test_recette_constructor_exists():
    assert callable(Recette.__init__)


def test_recette_constructor_args():
    sig = inspect.signature(Recette.__init__)
    params = list(sig.parameters.keys())
    assert "produit_id" in params, "Missing parameter 'produit_id'"
    assert "id" in params, "Missing parameter 'id'"

def test_recette_has_produit_id():
    assert hasattr(Recette, "produit_id")
    descriptor = None
    for klass in Recette.__mro__:
        if "produit_id" in klass.__dict__:
            descriptor = klass.__dict__["produit_id"]
            break
    assert isinstance(descriptor, property)

def test_recette_has_id():
    assert hasattr(Recette, "id")
    descriptor = None
    for klass in Recette.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_cat_gorie_is_not_abstract():
    assert not inspect.isabstract(Cat_gorie)


def test_cat_gorie_constructor_exists():
    assert callable(Cat_gorie.__init__)


def test_cat_gorie_constructor_args():
    sig = inspect.signature(Cat_gorie.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "nom" in params, "Missing parameter 'nom'"

def test_cat_gorie_has_id():
    assert hasattr(Cat_gorie, "id")
    descriptor = None
    for klass in Cat_gorie.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cat_gorie_has_nom():
    assert hasattr(Cat_gorie, "nom")
    descriptor = None
    for klass in Cat_gorie.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_ingr_dient_is_not_abstract():
    assert not inspect.isabstract(Ingr_dient)


def test_ingr_dient_constructor_exists():
    assert callable(Ingr_dient.__init__)


def test_ingr_dient_constructor_args():
    sig = inspect.signature(Ingr_dient.__init__)
    params = list(sig.parameters.keys())
    assert "poids" in params, "Missing parameter 'poids'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "unit_" in params, "Missing parameter 'unit_'"
    assert "id" in params, "Missing parameter 'id'"

def test_ingr_dient_has_poids():
    assert hasattr(Ingr_dient, "poids")
    descriptor = None
    for klass in Ingr_dient.__mro__:
        if "poids" in klass.__dict__:
            descriptor = klass.__dict__["poids"]
            break
    assert isinstance(descriptor, property)

def test_ingr_dient_has_nom():
    assert hasattr(Ingr_dient, "nom")
    descriptor = None
    for klass in Ingr_dient.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_ingr_dient_has_unit_():
    assert hasattr(Ingr_dient, "unit_")
    descriptor = None
    for klass in Ingr_dient.__mro__:
        if "unit_" in klass.__dict__:
            descriptor = klass.__dict__["unit_"]
            break
    assert isinstance(descriptor, property)

def test_ingr_dient_has_id():
    assert hasattr(Ingr_dient, "id")
    descriptor = None
    for klass in Ingr_dient.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_stock_is_not_abstract():
    assert not inspect.isabstract(Stock)


def test_stock_constructor_exists():
    assert callable(Stock.__init__)


def test_stock_constructor_args():
    sig = inspect.signature(Stock.__init__)
    params = list(sig.parameters.keys())
    assert "quantit_" in params, "Missing parameter 'quantit_'"
    assert "date_modification" in params, "Missing parameter 'date_modification'"
    assert "ingredient_id" in params, "Missing parameter 'ingredient_id'"
    assert "disponibilit_" in params, "Missing parameter 'disponibilit_'"

def test_stock_has_quantit_():
    assert hasattr(Stock, "quantit_")
    descriptor = None
    for klass in Stock.__mro__:
        if "quantit_" in klass.__dict__:
            descriptor = klass.__dict__["quantit_"]
            break
    assert isinstance(descriptor, property)

def test_stock_has_date_modification():
    assert hasattr(Stock, "date_modification")
    descriptor = None
    for klass in Stock.__mro__:
        if "date_modification" in klass.__dict__:
            descriptor = klass.__dict__["date_modification"]
            break
    assert isinstance(descriptor, property)

def test_stock_has_ingredient_id():
    assert hasattr(Stock, "ingredient_id")
    descriptor = None
    for klass in Stock.__mro__:
        if "ingredient_id" in klass.__dict__:
            descriptor = klass.__dict__["ingredient_id"]
            break
    assert isinstance(descriptor, property)

def test_stock_has_disponibilit_():
    assert hasattr(Stock, "disponibilit_")
    descriptor = None
    for klass in Stock.__mro__:
        if "disponibilit_" in klass.__dict__:
            descriptor = klass.__dict__["disponibilit_"]
            break
    assert isinstance(descriptor, property)



def test_livraison_is_not_abstract():
    assert not inspect.isabstract(Livraison)


def test_livraison_constructor_exists():
    assert callable(Livraison.__init__)


def test_livraison_constructor_args():
    sig = inspect.signature(Livraison.__init__)
    params = list(sig.parameters.keys())
    assert "client_id" in params, "Missing parameter 'client_id'"
    assert "geocode" in params, "Missing parameter 'geocode'"
    assert "livreur_id" in params, "Missing parameter 'livreur_id'"
    assert "id" in params, "Missing parameter 'id'"
    assert "commande_id" in params, "Missing parameter 'commande_id'"

def test_livraison_has_client_id():
    assert hasattr(Livraison, "client_id")
    descriptor = None
    for klass in Livraison.__mro__:
        if "client_id" in klass.__dict__:
            descriptor = klass.__dict__["client_id"]
            break
    assert isinstance(descriptor, property)

def test_livraison_has_geocode():
    assert hasattr(Livraison, "geocode")
    descriptor = None
    for klass in Livraison.__mro__:
        if "geocode" in klass.__dict__:
            descriptor = klass.__dict__["geocode"]
            break
    assert isinstance(descriptor, property)

def test_livraison_has_livreur_id():
    assert hasattr(Livraison, "livreur_id")
    descriptor = None
    for klass in Livraison.__mro__:
        if "livreur_id" in klass.__dict__:
            descriptor = klass.__dict__["livreur_id"]
            break
    assert isinstance(descriptor, property)

def test_livraison_has_id():
    assert hasattr(Livraison, "id")
    descriptor = None
    for klass in Livraison.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_livraison_has_commande_id():
    assert hasattr(Livraison, "commande_id")
    descriptor = None
    for klass in Livraison.__mro__:
        if "commande_id" in klass.__dict__:
            descriptor = klass.__dict__["commande_id"]
            break
    assert isinstance(descriptor, property)



def test_adresse_is_not_abstract():
    assert not inspect.isabstract(Adresse)


def test_adresse_constructor_exists():
    assert callable(Adresse.__init__)


def test_adresse_constructor_args():
    sig = inspect.signature(Adresse.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "ville" in params, "Missing parameter 'ville'"
    assert "t_l_phone" in params, "Missing parameter 't_l_phone'"
    assert "num_ro" in params, "Missing parameter 'num_ro'"
    assert "voie" in params, "Missing parameter 'voie'"
    assert "utilisateur_id" in params, "Missing parameter 'utilisateur_id'"
    assert "code_postal" in params, "Missing parameter 'code_postal'"
    assert "geocode" in params, "Missing parameter 'geocode'"

def test_adresse_has_id():
    assert hasattr(Adresse, "id")
    descriptor = None
    for klass in Adresse.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_adresse_has_ville():
    assert hasattr(Adresse, "ville")
    descriptor = None
    for klass in Adresse.__mro__:
        if "ville" in klass.__dict__:
            descriptor = klass.__dict__["ville"]
            break
    assert isinstance(descriptor, property)

def test_adresse_has_t_l_phone():
    assert hasattr(Adresse, "t_l_phone")
    descriptor = None
    for klass in Adresse.__mro__:
        if "t_l_phone" in klass.__dict__:
            descriptor = klass.__dict__["t_l_phone"]
            break
    assert isinstance(descriptor, property)

def test_adresse_has_num_ro():
    assert hasattr(Adresse, "num_ro")
    descriptor = None
    for klass in Adresse.__mro__:
        if "num_ro" in klass.__dict__:
            descriptor = klass.__dict__["num_ro"]
            break
    assert isinstance(descriptor, property)

def test_adresse_has_voie():
    assert hasattr(Adresse, "voie")
    descriptor = None
    for klass in Adresse.__mro__:
        if "voie" in klass.__dict__:
            descriptor = klass.__dict__["voie"]
            break
    assert isinstance(descriptor, property)

def test_adresse_has_utilisateur_id():
    assert hasattr(Adresse, "utilisateur_id")
    descriptor = None
    for klass in Adresse.__mro__:
        if "utilisateur_id" in klass.__dict__:
            descriptor = klass.__dict__["utilisateur_id"]
            break
    assert isinstance(descriptor, property)

def test_adresse_has_code_postal():
    assert hasattr(Adresse, "code_postal")
    descriptor = None
    for klass in Adresse.__mro__:
        if "code_postal" in klass.__dict__:
            descriptor = klass.__dict__["code_postal"]
            break
    assert isinstance(descriptor, property)

def test_adresse_has_geocode():
    assert hasattr(Adresse, "geocode")
    descriptor = None
    for klass in Adresse.__mro__:
        if "geocode" in klass.__dict__:
            descriptor = klass.__dict__["geocode"]
            break
    assert isinstance(descriptor, property)



def test_etat_is_not_abstract():
    assert not inspect.isabstract(Etat)


def test_etat_constructor_exists():
    assert callable(Etat.__init__)


def test_etat_constructor_args():
    sig = inspect.signature(Etat.__init__)
    params = list(sig.parameters.keys())
    assert "verrouillage" in params, "Missing parameter 'verrouillage'"
    assert "id" in params, "Missing parameter 'id'"
    assert "nom" in params, "Missing parameter 'nom'"

def test_etat_has_verrouillage():
    assert hasattr(Etat, "verrouillage")
    descriptor = None
    for klass in Etat.__mro__:
        if "verrouillage" in klass.__dict__:
            descriptor = klass.__dict__["verrouillage"]
            break
    assert isinstance(descriptor, property)

def test_etat_has_id():
    assert hasattr(Etat, "id")
    descriptor = None
    for klass in Etat.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etat_has_nom():
    assert hasattr(Etat, "nom")
    descriptor = None
    for klass in Etat.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_commande_is_not_abstract():
    assert not inspect.isabstract(Commande)


def test_commande_constructor_exists():
    assert callable(Commande.__init__)


def test_commande_constructor_args():
    sig = inspect.signature(Commande.__init__)
    params = list(sig.parameters.keys())
    assert "_tat" in params, "Missing parameter '_tat'"
    assert "date" in params, "Missing parameter 'date'"
    assert "id" in params, "Missing parameter 'id'"
    assert "utilisateur_id" in params, "Missing parameter 'utilisateur_id'"
    assert "paiement" in params, "Missing parameter 'paiement'"

def test_commande_has__tat():
    assert hasattr(Commande, "_tat")
    descriptor = None
    for klass in Commande.__mro__:
        if "_tat" in klass.__dict__:
            descriptor = klass.__dict__["_tat"]
            break
    assert isinstance(descriptor, property)

def test_commande_has_date():
    assert hasattr(Commande, "date")
    descriptor = None
    for klass in Commande.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_commande_has_id():
    assert hasattr(Commande, "id")
    descriptor = None
    for klass in Commande.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_commande_has_utilisateur_id():
    assert hasattr(Commande, "utilisateur_id")
    descriptor = None
    for klass in Commande.__mro__:
        if "utilisateur_id" in klass.__dict__:
            descriptor = klass.__dict__["utilisateur_id"]
            break
    assert isinstance(descriptor, property)

def test_commande_has_paiement():
    assert hasattr(Commande, "paiement")
    descriptor = None
    for klass in Commande.__mro__:
        if "paiement" in klass.__dict__:
            descriptor = klass.__dict__["paiement"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_utilisateur_is_not_abstract():
    assert not inspect.isabstract(Utilisateur)


def test_utilisateur_constructor_exists():
    assert callable(Utilisateur.__init__)


def test_utilisateur_constructor_args():
    sig = inspect.signature(Utilisateur.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "civilit_" in params, "Missing parameter 'civilit_'"
    assert "pizzeria_id" in params, "Missing parameter 'pizzeria_id'"
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "date_naissance" in params, "Missing parameter 'date_naissance'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "role_id" in params, "Missing parameter 'role_id'"
    assert "email" in params, "Missing parameter 'email'"
    assert "mot_de_passe" in params, "Missing parameter 'mot_de_passe'"

def test_utilisateur_has_id():
    assert hasattr(Utilisateur, "id")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_civilit_():
    assert hasattr(Utilisateur, "civilit_")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "civilit_" in klass.__dict__:
            descriptor = klass.__dict__["civilit_"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_pizzeria_id():
    assert hasattr(Utilisateur, "pizzeria_id")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "pizzeria_id" in klass.__dict__:
            descriptor = klass.__dict__["pizzeria_id"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_prenom():
    assert hasattr(Utilisateur, "prenom")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "prenom" in klass.__dict__:
            descriptor = klass.__dict__["prenom"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_date_naissance():
    assert hasattr(Utilisateur, "date_naissance")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "date_naissance" in klass.__dict__:
            descriptor = klass.__dict__["date_naissance"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_nom():
    assert hasattr(Utilisateur, "nom")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_role_id():
    assert hasattr(Utilisateur, "role_id")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "role_id" in klass.__dict__:
            descriptor = klass.__dict__["role_id"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_email():
    assert hasattr(Utilisateur, "email")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_mot_de_passe():
    assert hasattr(Utilisateur, "mot_de_passe")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "mot_de_passe" in klass.__dict__:
            descriptor = klass.__dict__["mot_de_passe"]
            break
    assert isinstance(descriptor, property)


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Pizzeria_strategy = st.builds(
    Pizzeria,
    nom=
        safe_text,
    id=
        st.integers(),
    adresse_id=
        st.integers()
)
R_le_strategy = st.builds(
    R_le,
    type=
        safe_text,
    id=
        st.integers()
)
Produit_strategy = st.builds(
    Produit,
    categorie_id=
        st.integers(),
    id=
        st.integers(),
    nom=
        safe_text,
    prix=
        safe_text
)
Recette_strategy = st.builds(
    Recette,
    produit_id=
        st.integers(),
    id=
        st.integers()
)
Cat_gorie_strategy = st.builds(
    Cat_gorie,
    id=
        st.integers(),
    nom=
        safe_text
)
Ingr_dient_strategy = st.builds(
    Ingr_dient,
    poids=
        safe_text,
    nom=
        safe_text,
    unit_=
        safe_text,
    id=
        st.integers()
)
Stock_strategy = st.builds(
    Stock,
    quantit_=
        st.integers(),
    date_modification=
        st.integers(),
    ingredient_id=
        st.integers(),
    disponibilit_=
        st.booleans()
)
Livraison_strategy = st.builds(
    Livraison,
    client_id=
        st.integers(),
    geocode=
        safe_text,
    livreur_id=
        st.integers(),
    id=
        st.integers(),
    commande_id=
        st.integers()
)
Adresse_strategy = st.builds(
    Adresse,
    id=
        st.integers(),
    ville=
        safe_text,
    t_l_phone=
        safe_text,
    num_ro=
        st.integers(),
    voie=
        safe_text,
    utilisateur_id=
        st.integers(),
    code_postal=
        st.integers(),
    geocode=
        safe_text
)
Etat_strategy = st.builds(
    Etat,
    verrouillage=
        st.booleans(),
    id=
        st.integers(),
    nom=
        safe_text
)
Commande_strategy = st.builds(
    Commande,
    _tat=
        st.integers(),
    date=
        st.integers(),
    id=
        st.integers(),
    utilisateur_id=
        st.integers(),
    paiement=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
Utilisateur_strategy = st.builds(
    Utilisateur,
    id=
        st.integers(),
    civilit_=
        safe_text,
    pizzeria_id=
        st.integers(),
    prenom=
        safe_text,
    date_naissance=
        safe_text,
    nom=
        safe_text,
    role_id=
        st.integers(),
    email=
        safe_text,
    mot_de_passe=
        safe_text
)

@given(instance=Pizzeria_strategy)
@settings(max_examples=50)
def test_pizzeria_instantiation(instance):
    assert isinstance(instance, Pizzeria)



@given(instance=Pizzeria_strategy)
def test_pizzeria_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Pizzeria_strategy)
def test_pizzeria_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Pizzeria_strategy)
def test_pizzeria_adresse_id_setter(instance):
    original = instance.adresse_id
    instance.adresse_id = original
    assert instance.adresse_id == original

@given(instance=R_le_strategy)
@settings(max_examples=50)
def test_r_le_instantiation(instance):
    assert isinstance(instance, R_le)



@given(instance=R_le_strategy)
def test_r_le_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=R_le_strategy)
def test_r_le_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Produit_strategy)
@settings(max_examples=50)
def test_produit_instantiation(instance):
    assert isinstance(instance, Produit)



@given(instance=Produit_strategy)
def test_produit_categorie_id_setter(instance):
    original = instance.categorie_id
    instance.categorie_id = original
    assert instance.categorie_id == original



@given(instance=Produit_strategy)
def test_produit_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Produit_strategy)
def test_produit_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Produit_strategy)
def test_produit_prix_setter(instance):
    original = instance.prix
    instance.prix = original
    assert instance.prix == original

@given(instance=Recette_strategy)
@settings(max_examples=50)
def test_recette_instantiation(instance):
    assert isinstance(instance, Recette)



@given(instance=Recette_strategy)
def test_recette_produit_id_setter(instance):
    original = instance.produit_id
    instance.produit_id = original
    assert instance.produit_id == original



@given(instance=Recette_strategy)
def test_recette_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Cat_gorie_strategy)
@settings(max_examples=50)
def test_cat_gorie_instantiation(instance):
    assert isinstance(instance, Cat_gorie)



@given(instance=Cat_gorie_strategy)
def test_cat_gorie_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Cat_gorie_strategy)
def test_cat_gorie_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=Ingr_dient_strategy)
@settings(max_examples=50)
def test_ingr_dient_instantiation(instance):
    assert isinstance(instance, Ingr_dient)



@given(instance=Ingr_dient_strategy)
def test_ingr_dient_poids_setter(instance):
    original = instance.poids
    instance.poids = original
    assert instance.poids == original



@given(instance=Ingr_dient_strategy)
def test_ingr_dient_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Ingr_dient_strategy)
def test_ingr_dient_unit__setter(instance):
    original = instance.unit_
    instance.unit_ = original
    assert instance.unit_ == original



@given(instance=Ingr_dient_strategy)
def test_ingr_dient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Stock_strategy)
@settings(max_examples=50)
def test_stock_instantiation(instance):
    assert isinstance(instance, Stock)



@given(instance=Stock_strategy)
def test_stock_quantit__setter(instance):
    original = instance.quantit_
    instance.quantit_ = original
    assert instance.quantit_ == original



@given(instance=Stock_strategy)
def test_stock_date_modification_setter(instance):
    original = instance.date_modification
    instance.date_modification = original
    assert instance.date_modification == original



@given(instance=Stock_strategy)
def test_stock_ingredient_id_setter(instance):
    original = instance.ingredient_id
    instance.ingredient_id = original
    assert instance.ingredient_id == original



@given(instance=Stock_strategy)
def test_stock_disponibilit__setter(instance):
    original = instance.disponibilit_
    instance.disponibilit_ = original
    assert instance.disponibilit_ == original

@given(instance=Livraison_strategy)
@settings(max_examples=50)
def test_livraison_instantiation(instance):
    assert isinstance(instance, Livraison)



@given(instance=Livraison_strategy)
def test_livraison_client_id_setter(instance):
    original = instance.client_id
    instance.client_id = original
    assert instance.client_id == original



@given(instance=Livraison_strategy)
def test_livraison_geocode_setter(instance):
    original = instance.geocode
    instance.geocode = original
    assert instance.geocode == original



@given(instance=Livraison_strategy)
def test_livraison_livreur_id_setter(instance):
    original = instance.livreur_id
    instance.livreur_id = original
    assert instance.livreur_id == original



@given(instance=Livraison_strategy)
def test_livraison_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Livraison_strategy)
def test_livraison_commande_id_setter(instance):
    original = instance.commande_id
    instance.commande_id = original
    assert instance.commande_id == original

@given(instance=Adresse_strategy)
@settings(max_examples=50)
def test_adresse_instantiation(instance):
    assert isinstance(instance, Adresse)



@given(instance=Adresse_strategy)
def test_adresse_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Adresse_strategy)
def test_adresse_ville_setter(instance):
    original = instance.ville
    instance.ville = original
    assert instance.ville == original



@given(instance=Adresse_strategy)
def test_adresse_t_l_phone_setter(instance):
    original = instance.t_l_phone
    instance.t_l_phone = original
    assert instance.t_l_phone == original



@given(instance=Adresse_strategy)
def test_adresse_num_ro_setter(instance):
    original = instance.num_ro
    instance.num_ro = original
    assert instance.num_ro == original



@given(instance=Adresse_strategy)
def test_adresse_voie_setter(instance):
    original = instance.voie
    instance.voie = original
    assert instance.voie == original



@given(instance=Adresse_strategy)
def test_adresse_utilisateur_id_setter(instance):
    original = instance.utilisateur_id
    instance.utilisateur_id = original
    assert instance.utilisateur_id == original



@given(instance=Adresse_strategy)
def test_adresse_code_postal_setter(instance):
    original = instance.code_postal
    instance.code_postal = original
    assert instance.code_postal == original



@given(instance=Adresse_strategy)
def test_adresse_geocode_setter(instance):
    original = instance.geocode
    instance.geocode = original
    assert instance.geocode == original

@given(instance=Etat_strategy)
@settings(max_examples=50)
def test_etat_instantiation(instance):
    assert isinstance(instance, Etat)



@given(instance=Etat_strategy)
def test_etat_verrouillage_setter(instance):
    original = instance.verrouillage
    instance.verrouillage = original
    assert instance.verrouillage == original



@given(instance=Etat_strategy)
def test_etat_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Etat_strategy)
def test_etat_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=Commande_strategy)
@settings(max_examples=50)
def test_commande_instantiation(instance):
    assert isinstance(instance, Commande)



@given(instance=Commande_strategy)
def test_commande__tat_setter(instance):
    original = instance._tat
    instance._tat = original
    assert instance._tat == original



@given(instance=Commande_strategy)
def test_commande_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Commande_strategy)
def test_commande_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Commande_strategy)
def test_commande_utilisateur_id_setter(instance):
    original = instance.utilisateur_id
    instance.utilisateur_id = original
    assert instance.utilisateur_id == original



@given(instance=Commande_strategy)
def test_commande_paiement_setter(instance):
    original = instance.paiement
    instance.paiement = original
    assert instance.paiement == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Utilisateur_strategy)
@settings(max_examples=50)
def test_utilisateur_instantiation(instance):
    assert isinstance(instance, Utilisateur)



@given(instance=Utilisateur_strategy)
def test_utilisateur_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_civilit__setter(instance):
    original = instance.civilit_
    instance.civilit_ = original
    assert instance.civilit_ == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_pizzeria_id_setter(instance):
    original = instance.pizzeria_id
    instance.pizzeria_id = original
    assert instance.pizzeria_id == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_date_naissance_setter(instance):
    original = instance.date_naissance
    instance.date_naissance = original
    assert instance.date_naissance == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_role_id_setter(instance):
    original = instance.role_id
    instance.role_id = original
    assert instance.role_id == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_mot_de_passe_setter(instance):
    original = instance.mot_de_passe
    instance.mot_de_passe = original
    assert instance.mot_de_passe == original
