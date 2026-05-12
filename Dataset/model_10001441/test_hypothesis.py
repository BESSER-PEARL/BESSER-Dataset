import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Controlleur_Actor,
    Analyse2_AvisGlobal,
    Analyse2_Moderateurs,
    Analyse2_Criteres,
    Analyse2_Compte,
    Analyse2_Utilisateur,
    Analyse2_Review,
    Analyse2_Fast_Food,
    Pr_sentation,
    Photo,
    Commentaire,
    AvisGlobal,
    FicheRestaurant,
    Analyse_Moderateurs,
    Analyse_Criteres,
    Analyse_Compte,
    Analyse_Utilisateur,
    Analyse_Review,
    Analyse_Fast_Food,
    Information,
    IHM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_controlleur_actor_is_not_abstract():
    assert not inspect.isabstract(Controlleur_Actor)


def test_controlleur_actor_constructor_exists():
    assert callable(Controlleur_Actor.__init__)


def test_controlleur_actor_constructor_args():
    sig = inspect.signature(Controlleur_Actor.__init__)
    params = list(sig.parameters.keys())



def test_analyse2_avisglobal_is_not_abstract():
    assert not inspect.isabstract(Analyse2_AvisGlobal)


def test_analyse2_avisglobal_constructor_exists():
    assert callable(Analyse2_AvisGlobal.__init__)


def test_analyse2_avisglobal_constructor_args():
    sig = inspect.signature(Analyse2_AvisGlobal.__init__)
    params = list(sig.parameters.keys())
    assert "notes" in params, "Missing parameter 'notes'"
    assert "Commentaires" in params, "Missing parameter 'Commentaires'"
    assert "nbAvis" in params, "Missing parameter 'nbAvis'"

def test_analyse2_avisglobal_has_notes():
    assert hasattr(Analyse2_AvisGlobal, "notes")
    descriptor = None
    for klass in Analyse2_AvisGlobal.__mro__:
        if "notes" in klass.__dict__:
            descriptor = klass.__dict__["notes"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_avisglobal_has_Commentaires():
    assert hasattr(Analyse2_AvisGlobal, "Commentaires")
    descriptor = None
    for klass in Analyse2_AvisGlobal.__mro__:
        if "Commentaires" in klass.__dict__:
            descriptor = klass.__dict__["Commentaires"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_avisglobal_has_nbAvis():
    assert hasattr(Analyse2_AvisGlobal, "nbAvis")
    descriptor = None
    for klass in Analyse2_AvisGlobal.__mro__:
        if "nbAvis" in klass.__dict__:
            descriptor = klass.__dict__["nbAvis"]
            break
    assert isinstance(descriptor, property)



def test_analyse2_moderateurs_is_not_abstract():
    assert not inspect.isabstract(Analyse2_Moderateurs)


def test_analyse2_moderateurs_constructor_exists():
    assert callable(Analyse2_Moderateurs.__init__)


def test_analyse2_moderateurs_constructor_args():
    sig = inspect.signature(Analyse2_Moderateurs.__init__)
    params = list(sig.parameters.keys())



def test_analyse2_criteres_is_not_abstract():
    assert not inspect.isabstract(Analyse2_Criteres)


def test_analyse2_criteres_constructor_exists():
    assert callable(Analyse2_Criteres.__init__)


def test_analyse2_criteres_constructor_args():
    sig = inspect.signature(Analyse2_Criteres.__init__)
    params = list(sig.parameters.keys())
    assert "qualit_" in params, "Missing parameter 'qualit_'"
    assert "rapportQualitePrix" in params, "Missing parameter 'rapportQualitePrix'"
    assert "rapidite" in params, "Missing parameter 'rapidite'"
    assert "amabilite" in params, "Missing parameter 'amabilite'"
    assert "respectHoraires" in params, "Missing parameter 'respectHoraires'"

def test_analyse2_criteres_has_qualit_():
    assert hasattr(Analyse2_Criteres, "qualit_")
    descriptor = None
    for klass in Analyse2_Criteres.__mro__:
        if "qualit_" in klass.__dict__:
            descriptor = klass.__dict__["qualit_"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_criteres_has_rapportQualitePrix():
    assert hasattr(Analyse2_Criteres, "rapportQualitePrix")
    descriptor = None
    for klass in Analyse2_Criteres.__mro__:
        if "rapportQualitePrix" in klass.__dict__:
            descriptor = klass.__dict__["rapportQualitePrix"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_criteres_has_rapidite():
    assert hasattr(Analyse2_Criteres, "rapidite")
    descriptor = None
    for klass in Analyse2_Criteres.__mro__:
        if "rapidite" in klass.__dict__:
            descriptor = klass.__dict__["rapidite"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_criteres_has_amabilite():
    assert hasattr(Analyse2_Criteres, "amabilite")
    descriptor = None
    for klass in Analyse2_Criteres.__mro__:
        if "amabilite" in klass.__dict__:
            descriptor = klass.__dict__["amabilite"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_criteres_has_respectHoraires():
    assert hasattr(Analyse2_Criteres, "respectHoraires")
    descriptor = None
    for klass in Analyse2_Criteres.__mro__:
        if "respectHoraires" in klass.__dict__:
            descriptor = klass.__dict__["respectHoraires"]
            break
    assert isinstance(descriptor, property)



def test_analyse2_compte_is_not_abstract():
    assert not inspect.isabstract(Analyse2_Compte)


def test_analyse2_compte_constructor_exists():
    assert callable(Analyse2_Compte.__init__)


def test_analyse2_compte_constructor_args():
    sig = inspect.signature(Analyse2_Compte.__init__)
    params = list(sig.parameters.keys())
    assert "login" in params, "Missing parameter 'login'"
    assert "motdepasse" in params, "Missing parameter 'motdepasse'"

def test_analyse2_compte_has_login():
    assert hasattr(Analyse2_Compte, "login")
    descriptor = None
    for klass in Analyse2_Compte.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_compte_has_motdepasse():
    assert hasattr(Analyse2_Compte, "motdepasse")
    descriptor = None
    for klass in Analyse2_Compte.__mro__:
        if "motdepasse" in klass.__dict__:
            descriptor = klass.__dict__["motdepasse"]
            break
    assert isinstance(descriptor, property)



def test_analyse2_utilisateur_is_not_abstract():
    assert not inspect.isabstract(Analyse2_Utilisateur)


def test_analyse2_utilisateur_constructor_exists():
    assert callable(Analyse2_Utilisateur.__init__)


def test_analyse2_utilisateur_constructor_args():
    sig = inspect.signature(Analyse2_Utilisateur.__init__)
    params = list(sig.parameters.keys())



def test_analyse2_review_is_not_abstract():
    assert not inspect.isabstract(Analyse2_Review)


def test_analyse2_review_constructor_exists():
    assert callable(Analyse2_Review.__init__)


def test_analyse2_review_constructor_args():
    sig = inspect.signature(Analyse2_Review.__init__)
    params = list(sig.parameters.keys())
    assert "lesNotes" in params, "Missing parameter 'lesNotes'"
    assert "utilite" in params, "Missing parameter 'utilite'"
    assert "Commentaire" in params, "Missing parameter 'Commentaire'"

def test_analyse2_review_has_lesNotes():
    assert hasattr(Analyse2_Review, "lesNotes")
    descriptor = None
    for klass in Analyse2_Review.__mro__:
        if "lesNotes" in klass.__dict__:
            descriptor = klass.__dict__["lesNotes"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_review_has_utilite():
    assert hasattr(Analyse2_Review, "utilite")
    descriptor = None
    for klass in Analyse2_Review.__mro__:
        if "utilite" in klass.__dict__:
            descriptor = klass.__dict__["utilite"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_review_has_Commentaire():
    assert hasattr(Analyse2_Review, "Commentaire")
    descriptor = None
    for klass in Analyse2_Review.__mro__:
        if "Commentaire" in klass.__dict__:
            descriptor = klass.__dict__["Commentaire"]
            break
    assert isinstance(descriptor, property)



def test_analyse2_fast_food_is_not_abstract():
    assert not inspect.isabstract(Analyse2_Fast_Food)


def test_analyse2_fast_food_constructor_exists():
    assert callable(Analyse2_Fast_Food.__init__)


def test_analyse2_fast_food_constructor_args():
    sig = inspect.signature(Analyse2_Fast_Food.__init__)
    params = list(sig.parameters.keys())
    assert "prixMin" in params, "Missing parameter 'prixMin'"
    assert "proprietaire" in params, "Missing parameter 'proprietaire'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "nbPlaces" in params, "Missing parameter 'nbPlaces'"
    assert "prixMax" in params, "Missing parameter 'prixMax'"
    assert "photos" in params, "Missing parameter 'photos'"
    assert "siteDeCommande" in params, "Missing parameter 'siteDeCommande'"
    assert "Ville" in params, "Missing parameter 'Ville'"
    assert "horaires" in params, "Missing parameter 'horaires'"
    assert "description" in params, "Missing parameter 'description'"
    assert "reviews" in params, "Missing parameter 'reviews'"
    assert "numeroTel" in params, "Missing parameter 'numeroTel'"
    assert "Adresse" in params, "Missing parameter 'Adresse'"

def test_analyse2_fast_food_has_prixMin():
    assert hasattr(Analyse2_Fast_Food, "prixMin")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "prixMin" in klass.__dict__:
            descriptor = klass.__dict__["prixMin"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_proprietaire():
    assert hasattr(Analyse2_Fast_Food, "proprietaire")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "proprietaire" in klass.__dict__:
            descriptor = klass.__dict__["proprietaire"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_nom():
    assert hasattr(Analyse2_Fast_Food, "nom")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_nbPlaces():
    assert hasattr(Analyse2_Fast_Food, "nbPlaces")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "nbPlaces" in klass.__dict__:
            descriptor = klass.__dict__["nbPlaces"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_prixMax():
    assert hasattr(Analyse2_Fast_Food, "prixMax")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "prixMax" in klass.__dict__:
            descriptor = klass.__dict__["prixMax"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_photos():
    assert hasattr(Analyse2_Fast_Food, "photos")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "photos" in klass.__dict__:
            descriptor = klass.__dict__["photos"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_siteDeCommande():
    assert hasattr(Analyse2_Fast_Food, "siteDeCommande")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "siteDeCommande" in klass.__dict__:
            descriptor = klass.__dict__["siteDeCommande"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_Ville():
    assert hasattr(Analyse2_Fast_Food, "Ville")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "Ville" in klass.__dict__:
            descriptor = klass.__dict__["Ville"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_horaires():
    assert hasattr(Analyse2_Fast_Food, "horaires")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "horaires" in klass.__dict__:
            descriptor = klass.__dict__["horaires"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_description():
    assert hasattr(Analyse2_Fast_Food, "description")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_reviews():
    assert hasattr(Analyse2_Fast_Food, "reviews")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "reviews" in klass.__dict__:
            descriptor = klass.__dict__["reviews"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_numeroTel():
    assert hasattr(Analyse2_Fast_Food, "numeroTel")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "numeroTel" in klass.__dict__:
            descriptor = klass.__dict__["numeroTel"]
            break
    assert isinstance(descriptor, property)

def test_analyse2_fast_food_has_Adresse():
    assert hasattr(Analyse2_Fast_Food, "Adresse")
    descriptor = None
    for klass in Analyse2_Fast_Food.__mro__:
        if "Adresse" in klass.__dict__:
            descriptor = klass.__dict__["Adresse"]
            break
    assert isinstance(descriptor, property)



def test_pr_sentation_is_not_abstract():
    assert not inspect.isabstract(Pr_sentation)


def test_pr_sentation_constructor_exists():
    assert callable(Pr_sentation.__init__)


def test_pr_sentation_constructor_args():
    sig = inspect.signature(Pr_sentation.__init__)
    params = list(sig.parameters.keys())
    assert "numTel" in params, "Missing parameter 'numTel'"
    assert "adresse" in params, "Missing parameter 'adresse'"
    assert "ouverture" in params, "Missing parameter 'ouverture'"
    assert "description" in params, "Missing parameter 'description'"
    assert "siteDeCommande" in params, "Missing parameter 'siteDeCommande'"

def test_pr_sentation_has_numTel():
    assert hasattr(Pr_sentation, "numTel")
    descriptor = None
    for klass in Pr_sentation.__mro__:
        if "numTel" in klass.__dict__:
            descriptor = klass.__dict__["numTel"]
            break
    assert isinstance(descriptor, property)

def test_pr_sentation_has_adresse():
    assert hasattr(Pr_sentation, "adresse")
    descriptor = None
    for klass in Pr_sentation.__mro__:
        if "adresse" in klass.__dict__:
            descriptor = klass.__dict__["adresse"]
            break
    assert isinstance(descriptor, property)

def test_pr_sentation_has_ouverture():
    assert hasattr(Pr_sentation, "ouverture")
    descriptor = None
    for klass in Pr_sentation.__mro__:
        if "ouverture" in klass.__dict__:
            descriptor = klass.__dict__["ouverture"]
            break
    assert isinstance(descriptor, property)

def test_pr_sentation_has_description():
    assert hasattr(Pr_sentation, "description")
    descriptor = None
    for klass in Pr_sentation.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_pr_sentation_has_siteDeCommande():
    assert hasattr(Pr_sentation, "siteDeCommande")
    descriptor = None
    for klass in Pr_sentation.__mro__:
        if "siteDeCommande" in klass.__dict__:
            descriptor = klass.__dict__["siteDeCommande"]
            break
    assert isinstance(descriptor, property)



def test_photo_is_not_abstract():
    assert not inspect.isabstract(Photo)


def test_photo_constructor_exists():
    assert callable(Photo.__init__)


def test_photo_constructor_args():
    sig = inspect.signature(Photo.__init__)
    params = list(sig.parameters.keys())



def test_commentaire_is_not_abstract():
    assert not inspect.isabstract(Commentaire)


def test_commentaire_constructor_exists():
    assert callable(Commentaire.__init__)


def test_commentaire_constructor_args():
    sig = inspect.signature(Commentaire.__init__)
    params = list(sig.parameters.keys())
    assert "commentaire" in params, "Missing parameter 'commentaire'"
    assert "auteur" in params, "Missing parameter 'auteur'"

def test_commentaire_has_commentaire():
    assert hasattr(Commentaire, "commentaire")
    descriptor = None
    for klass in Commentaire.__mro__:
        if "commentaire" in klass.__dict__:
            descriptor = klass.__dict__["commentaire"]
            break
    assert isinstance(descriptor, property)

def test_commentaire_has_auteur():
    assert hasattr(Commentaire, "auteur")
    descriptor = None
    for klass in Commentaire.__mro__:
        if "auteur" in klass.__dict__:
            descriptor = klass.__dict__["auteur"]
            break
    assert isinstance(descriptor, property)



def test_avisglobal_is_not_abstract():
    assert not inspect.isabstract(AvisGlobal)


def test_avisglobal_constructor_exists():
    assert callable(AvisGlobal.__init__)


def test_avisglobal_constructor_args():
    sig = inspect.signature(AvisGlobal.__init__)
    params = list(sig.parameters.keys())
    assert "nbAvis" in params, "Missing parameter 'nbAvis'"
    assert "diagramme" in params, "Missing parameter 'diagramme'"
    assert "note" in params, "Missing parameter 'note'"
    assert "Commentaires" in params, "Missing parameter 'Commentaires'"

def test_avisglobal_has_nbAvis():
    assert hasattr(AvisGlobal, "nbAvis")
    descriptor = None
    for klass in AvisGlobal.__mro__:
        if "nbAvis" in klass.__dict__:
            descriptor = klass.__dict__["nbAvis"]
            break
    assert isinstance(descriptor, property)

def test_avisglobal_has_diagramme():
    assert hasattr(AvisGlobal, "diagramme")
    descriptor = None
    for klass in AvisGlobal.__mro__:
        if "diagramme" in klass.__dict__:
            descriptor = klass.__dict__["diagramme"]
            break
    assert isinstance(descriptor, property)

def test_avisglobal_has_note():
    assert hasattr(AvisGlobal, "note")
    descriptor = None
    for klass in AvisGlobal.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_avisglobal_has_Commentaires():
    assert hasattr(AvisGlobal, "Commentaires")
    descriptor = None
    for klass in AvisGlobal.__mro__:
        if "Commentaires" in klass.__dict__:
            descriptor = klass.__dict__["Commentaires"]
            break
    assert isinstance(descriptor, property)



def test_ficherestaurant_is_not_abstract():
    assert not inspect.isabstract(FicheRestaurant)


def test_ficherestaurant_constructor_exists():
    assert callable(FicheRestaurant.__init__)


def test_ficherestaurant_constructor_args():
    sig = inspect.signature(FicheRestaurant.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_ficherestaurant_has_nom():
    assert hasattr(FicheRestaurant, "nom")
    descriptor = None
    for klass in FicheRestaurant.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_analyse_moderateurs_is_not_abstract():
    assert not inspect.isabstract(Analyse_Moderateurs)


def test_analyse_moderateurs_constructor_exists():
    assert callable(Analyse_Moderateurs.__init__)


def test_analyse_moderateurs_constructor_args():
    sig = inspect.signature(Analyse_Moderateurs.__init__)
    params = list(sig.parameters.keys())



def test_analyse_criteres_is_not_abstract():
    assert not inspect.isabstract(Analyse_Criteres)


def test_analyse_criteres_constructor_exists():
    assert callable(Analyse_Criteres.__init__)


def test_analyse_criteres_constructor_args():
    sig = inspect.signature(Analyse_Criteres.__init__)
    params = list(sig.parameters.keys())
    assert "respectHoraires" in params, "Missing parameter 'respectHoraires'"
    assert "rapidite" in params, "Missing parameter 'rapidite'"
    assert "qualit_" in params, "Missing parameter 'qualit_'"
    assert "rapportQualitePrix" in params, "Missing parameter 'rapportQualitePrix'"
    assert "amabilite" in params, "Missing parameter 'amabilite'"

def test_analyse_criteres_has_respectHoraires():
    assert hasattr(Analyse_Criteres, "respectHoraires")
    descriptor = None
    for klass in Analyse_Criteres.__mro__:
        if "respectHoraires" in klass.__dict__:
            descriptor = klass.__dict__["respectHoraires"]
            break
    assert isinstance(descriptor, property)

def test_analyse_criteres_has_rapidite():
    assert hasattr(Analyse_Criteres, "rapidite")
    descriptor = None
    for klass in Analyse_Criteres.__mro__:
        if "rapidite" in klass.__dict__:
            descriptor = klass.__dict__["rapidite"]
            break
    assert isinstance(descriptor, property)

def test_analyse_criteres_has_qualit_():
    assert hasattr(Analyse_Criteres, "qualit_")
    descriptor = None
    for klass in Analyse_Criteres.__mro__:
        if "qualit_" in klass.__dict__:
            descriptor = klass.__dict__["qualit_"]
            break
    assert isinstance(descriptor, property)

def test_analyse_criteres_has_rapportQualitePrix():
    assert hasattr(Analyse_Criteres, "rapportQualitePrix")
    descriptor = None
    for klass in Analyse_Criteres.__mro__:
        if "rapportQualitePrix" in klass.__dict__:
            descriptor = klass.__dict__["rapportQualitePrix"]
            break
    assert isinstance(descriptor, property)

def test_analyse_criteres_has_amabilite():
    assert hasattr(Analyse_Criteres, "amabilite")
    descriptor = None
    for klass in Analyse_Criteres.__mro__:
        if "amabilite" in klass.__dict__:
            descriptor = klass.__dict__["amabilite"]
            break
    assert isinstance(descriptor, property)



def test_analyse_compte_is_not_abstract():
    assert not inspect.isabstract(Analyse_Compte)


def test_analyse_compte_constructor_exists():
    assert callable(Analyse_Compte.__init__)


def test_analyse_compte_constructor_args():
    sig = inspect.signature(Analyse_Compte.__init__)
    params = list(sig.parameters.keys())
    assert "motdepasse" in params, "Missing parameter 'motdepasse'"
    assert "login" in params, "Missing parameter 'login'"

def test_analyse_compte_has_motdepasse():
    assert hasattr(Analyse_Compte, "motdepasse")
    descriptor = None
    for klass in Analyse_Compte.__mro__:
        if "motdepasse" in klass.__dict__:
            descriptor = klass.__dict__["motdepasse"]
            break
    assert isinstance(descriptor, property)

def test_analyse_compte_has_login():
    assert hasattr(Analyse_Compte, "login")
    descriptor = None
    for klass in Analyse_Compte.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)



def test_analyse_utilisateur_is_not_abstract():
    assert not inspect.isabstract(Analyse_Utilisateur)


def test_analyse_utilisateur_constructor_exists():
    assert callable(Analyse_Utilisateur.__init__)


def test_analyse_utilisateur_constructor_args():
    sig = inspect.signature(Analyse_Utilisateur.__init__)
    params = list(sig.parameters.keys())



def test_analyse_review_is_not_abstract():
    assert not inspect.isabstract(Analyse_Review)


def test_analyse_review_constructor_exists():
    assert callable(Analyse_Review.__init__)


def test_analyse_review_constructor_args():
    sig = inspect.signature(Analyse_Review.__init__)
    params = list(sig.parameters.keys())
    assert "lesNotes" in params, "Missing parameter 'lesNotes'"
    assert "NoteGlobale" in params, "Missing parameter 'NoteGlobale'"
    assert "Commentaire" in params, "Missing parameter 'Commentaire'"

def test_analyse_review_has_lesNotes():
    assert hasattr(Analyse_Review, "lesNotes")
    descriptor = None
    for klass in Analyse_Review.__mro__:
        if "lesNotes" in klass.__dict__:
            descriptor = klass.__dict__["lesNotes"]
            break
    assert isinstance(descriptor, property)

def test_analyse_review_has_NoteGlobale():
    assert hasattr(Analyse_Review, "NoteGlobale")
    descriptor = None
    for klass in Analyse_Review.__mro__:
        if "NoteGlobale" in klass.__dict__:
            descriptor = klass.__dict__["NoteGlobale"]
            break
    assert isinstance(descriptor, property)

def test_analyse_review_has_Commentaire():
    assert hasattr(Analyse_Review, "Commentaire")
    descriptor = None
    for klass in Analyse_Review.__mro__:
        if "Commentaire" in klass.__dict__:
            descriptor = klass.__dict__["Commentaire"]
            break
    assert isinstance(descriptor, property)



def test_analyse_fast_food_is_not_abstract():
    assert not inspect.isabstract(Analyse_Fast_Food)


def test_analyse_fast_food_constructor_exists():
    assert callable(Analyse_Fast_Food.__init__)


def test_analyse_fast_food_constructor_args():
    sig = inspect.signature(Analyse_Fast_Food.__init__)
    params = list(sig.parameters.keys())
    assert "numeroTel" in params, "Missing parameter 'numeroTel'"
    assert "photos" in params, "Missing parameter 'photos'"
    assert "prixMax" in params, "Missing parameter 'prixMax'"
    assert "horaires" in params, "Missing parameter 'horaires'"
    assert "Adresse" in params, "Missing parameter 'Adresse'"
    assert "Ville" in params, "Missing parameter 'Ville'"
    assert "prixMin" in params, "Missing parameter 'prixMin'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "nbPlaces" in params, "Missing parameter 'nbPlaces'"
    assert "notes" in params, "Missing parameter 'notes'"
    assert "proprietaire" in params, "Missing parameter 'proprietaire'"

def test_analyse_fast_food_has_numeroTel():
    assert hasattr(Analyse_Fast_Food, "numeroTel")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "numeroTel" in klass.__dict__:
            descriptor = klass.__dict__["numeroTel"]
            break
    assert isinstance(descriptor, property)

def test_analyse_fast_food_has_photos():
    assert hasattr(Analyse_Fast_Food, "photos")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "photos" in klass.__dict__:
            descriptor = klass.__dict__["photos"]
            break
    assert isinstance(descriptor, property)

def test_analyse_fast_food_has_prixMax():
    assert hasattr(Analyse_Fast_Food, "prixMax")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "prixMax" in klass.__dict__:
            descriptor = klass.__dict__["prixMax"]
            break
    assert isinstance(descriptor, property)

def test_analyse_fast_food_has_horaires():
    assert hasattr(Analyse_Fast_Food, "horaires")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "horaires" in klass.__dict__:
            descriptor = klass.__dict__["horaires"]
            break
    assert isinstance(descriptor, property)

def test_analyse_fast_food_has_Adresse():
    assert hasattr(Analyse_Fast_Food, "Adresse")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "Adresse" in klass.__dict__:
            descriptor = klass.__dict__["Adresse"]
            break
    assert isinstance(descriptor, property)

def test_analyse_fast_food_has_Ville():
    assert hasattr(Analyse_Fast_Food, "Ville")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "Ville" in klass.__dict__:
            descriptor = klass.__dict__["Ville"]
            break
    assert isinstance(descriptor, property)

def test_analyse_fast_food_has_prixMin():
    assert hasattr(Analyse_Fast_Food, "prixMin")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "prixMin" in klass.__dict__:
            descriptor = klass.__dict__["prixMin"]
            break
    assert isinstance(descriptor, property)

def test_analyse_fast_food_has_nom():
    assert hasattr(Analyse_Fast_Food, "nom")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_analyse_fast_food_has_nbPlaces():
    assert hasattr(Analyse_Fast_Food, "nbPlaces")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "nbPlaces" in klass.__dict__:
            descriptor = klass.__dict__["nbPlaces"]
            break
    assert isinstance(descriptor, property)

def test_analyse_fast_food_has_notes():
    assert hasattr(Analyse_Fast_Food, "notes")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "notes" in klass.__dict__:
            descriptor = klass.__dict__["notes"]
            break
    assert isinstance(descriptor, property)

def test_analyse_fast_food_has_proprietaire():
    assert hasattr(Analyse_Fast_Food, "proprietaire")
    descriptor = None
    for klass in Analyse_Fast_Food.__mro__:
        if "proprietaire" in klass.__dict__:
            descriptor = klass.__dict__["proprietaire"]
            break
    assert isinstance(descriptor, property)

def test_information_exists():
    # Check that the Enumeration exists
    assert Information is not None

def test_information_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Information]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Information"

def test_ihm_exists():
    # Check that the Enumeration exists
    assert IHM is not None

def test_ihm_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IHM]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IHM"


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
Controlleur_Actor_strategy = st.builds(
    Controlleur_Actor,
)
Analyse2_AvisGlobal_strategy = st.builds(
    Analyse2_AvisGlobal,
    notes=
        safe_text,
    Commentaires=
        safe_text,
    nbAvis=
        st.integers()
)
Analyse2_Moderateurs_strategy = st.builds(
    Analyse2_Moderateurs,
)
Analyse2_Criteres_strategy = st.builds(
    Analyse2_Criteres,
    qualit_=
        st.integers(),
    rapportQualitePrix=
        st.integers(),
    rapidite=
        st.integers(),
    amabilite=
        st.integers(),
    respectHoraires=
        st.integers()
)
Analyse2_Compte_strategy = st.builds(
    Analyse2_Compte,
    login=
        safe_text,
    motdepasse=
        safe_text
)
Analyse2_Utilisateur_strategy = st.builds(
    Analyse2_Utilisateur,
)
Analyse2_Review_strategy = st.builds(
    Analyse2_Review,
    lesNotes=
        safe_text,
    utilite=
        safe_text,
    Commentaire=
        safe_text
)
Analyse2_Fast_Food_strategy = st.builds(
    Analyse2_Fast_Food,
    prixMin=
        st.integers(),
    proprietaire=
        safe_text,
    nom=
        safe_text,
    nbPlaces=
        st.integers(),
    prixMax=
        st.integers(),
    photos=
        safe_text,
    siteDeCommande=
        safe_text,
    Ville=
        safe_text,
    horaires=
        safe_text,
    description=
        safe_text,
    reviews=
        safe_text,
    numeroTel=
        safe_text,
    Adresse=
        safe_text
)
Pr_sentation_strategy = st.builds(
    Pr_sentation,
    numTel=
        safe_text,
    adresse=
        safe_text,
    ouverture=
        safe_text,
    description=
        safe_text,
    siteDeCommande=
        safe_text
)
Photo_strategy = st.builds(
    Photo,
)
Commentaire_strategy = st.builds(
    Commentaire,
    commentaire=
        safe_text,
    auteur=
        st.none()
)
AvisGlobal_strategy = st.builds(
    AvisGlobal,
    nbAvis=
        st.integers(),
    diagramme=
        safe_text,
    note=
        safe_text,
    Commentaires=
        safe_text
)
FicheRestaurant_strategy = st.builds(
    FicheRestaurant,
    nom=
        safe_text
)
Analyse_Moderateurs_strategy = st.builds(
    Analyse_Moderateurs,
)
Analyse_Criteres_strategy = st.builds(
    Analyse_Criteres,
    respectHoraires=
        st.integers(),
    rapidite=
        st.integers(),
    qualit_=
        st.integers(),
    rapportQualitePrix=
        st.integers(),
    amabilite=
        st.integers()
)
Analyse_Compte_strategy = st.builds(
    Analyse_Compte,
    motdepasse=
        safe_text,
    login=
        safe_text
)
Analyse_Utilisateur_strategy = st.builds(
    Analyse_Utilisateur,
)
Analyse_Review_strategy = st.builds(
    Analyse_Review,
    lesNotes=
        safe_text,
    NoteGlobale=
        st.integers(),
    Commentaire=
        safe_text
)
Analyse_Fast_Food_strategy = st.builds(
    Analyse_Fast_Food,
    numeroTel=
        safe_text,
    photos=
        safe_text,
    prixMax=
        st.integers(),
    horaires=
        safe_text,
    Adresse=
        safe_text,
    Ville=
        safe_text,
    prixMin=
        st.integers(),
    nom=
        safe_text,
    nbPlaces=
        st.integers(),
    notes=
        safe_text,
    proprietaire=
        safe_text
)

@given(instance=Controlleur_Actor_strategy)
@settings(max_examples=50)
def test_controlleur_actor_instantiation(instance):
    assert isinstance(instance, Controlleur_Actor)

@given(instance=Analyse2_AvisGlobal_strategy)
@settings(max_examples=50)
def test_analyse2_avisglobal_instantiation(instance):
    assert isinstance(instance, Analyse2_AvisGlobal)



@given(instance=Analyse2_AvisGlobal_strategy)
def test_analyse2_avisglobal_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=Analyse2_AvisGlobal_strategy)
def test_analyse2_avisglobal_Commentaires_setter(instance):
    original = instance.Commentaires
    instance.Commentaires = original
    assert instance.Commentaires == original



@given(instance=Analyse2_AvisGlobal_strategy)
def test_analyse2_avisglobal_nbAvis_setter(instance):
    original = instance.nbAvis
    instance.nbAvis = original
    assert instance.nbAvis == original

@given(instance=Analyse2_Moderateurs_strategy)
@settings(max_examples=50)
def test_analyse2_moderateurs_instantiation(instance):
    assert isinstance(instance, Analyse2_Moderateurs)

@given(instance=Analyse2_Criteres_strategy)
@settings(max_examples=50)
def test_analyse2_criteres_instantiation(instance):
    assert isinstance(instance, Analyse2_Criteres)



@given(instance=Analyse2_Criteres_strategy)
def test_analyse2_criteres_qualit__setter(instance):
    original = instance.qualit_
    instance.qualit_ = original
    assert instance.qualit_ == original



@given(instance=Analyse2_Criteres_strategy)
def test_analyse2_criteres_rapportQualitePrix_setter(instance):
    original = instance.rapportQualitePrix
    instance.rapportQualitePrix = original
    assert instance.rapportQualitePrix == original



@given(instance=Analyse2_Criteres_strategy)
def test_analyse2_criteres_rapidite_setter(instance):
    original = instance.rapidite
    instance.rapidite = original
    assert instance.rapidite == original



@given(instance=Analyse2_Criteres_strategy)
def test_analyse2_criteres_amabilite_setter(instance):
    original = instance.amabilite
    instance.amabilite = original
    assert instance.amabilite == original



@given(instance=Analyse2_Criteres_strategy)
def test_analyse2_criteres_respectHoraires_setter(instance):
    original = instance.respectHoraires
    instance.respectHoraires = original
    assert instance.respectHoraires == original

@given(instance=Analyse2_Compte_strategy)
@settings(max_examples=50)
def test_analyse2_compte_instantiation(instance):
    assert isinstance(instance, Analyse2_Compte)



@given(instance=Analyse2_Compte_strategy)
def test_analyse2_compte_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=Analyse2_Compte_strategy)
def test_analyse2_compte_motdepasse_setter(instance):
    original = instance.motdepasse
    instance.motdepasse = original
    assert instance.motdepasse == original

@given(instance=Analyse2_Utilisateur_strategy)
@settings(max_examples=50)
def test_analyse2_utilisateur_instantiation(instance):
    assert isinstance(instance, Analyse2_Utilisateur)

@given(instance=Analyse2_Review_strategy)
@settings(max_examples=50)
def test_analyse2_review_instantiation(instance):
    assert isinstance(instance, Analyse2_Review)



@given(instance=Analyse2_Review_strategy)
def test_analyse2_review_lesNotes_setter(instance):
    original = instance.lesNotes
    instance.lesNotes = original
    assert instance.lesNotes == original



@given(instance=Analyse2_Review_strategy)
def test_analyse2_review_utilite_setter(instance):
    original = instance.utilite
    instance.utilite = original
    assert instance.utilite == original



@given(instance=Analyse2_Review_strategy)
def test_analyse2_review_Commentaire_setter(instance):
    original = instance.Commentaire
    instance.Commentaire = original
    assert instance.Commentaire == original

@given(instance=Analyse2_Fast_Food_strategy)
@settings(max_examples=50)
def test_analyse2_fast_food_instantiation(instance):
    assert isinstance(instance, Analyse2_Fast_Food)



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_prixMin_setter(instance):
    original = instance.prixMin
    instance.prixMin = original
    assert instance.prixMin == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_proprietaire_setter(instance):
    original = instance.proprietaire
    instance.proprietaire = original
    assert instance.proprietaire == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_nbPlaces_setter(instance):
    original = instance.nbPlaces
    instance.nbPlaces = original
    assert instance.nbPlaces == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_prixMax_setter(instance):
    original = instance.prixMax
    instance.prixMax = original
    assert instance.prixMax == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_photos_setter(instance):
    original = instance.photos
    instance.photos = original
    assert instance.photos == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_siteDeCommande_setter(instance):
    original = instance.siteDeCommande
    instance.siteDeCommande = original
    assert instance.siteDeCommande == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_Ville_setter(instance):
    original = instance.Ville
    instance.Ville = original
    assert instance.Ville == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_horaires_setter(instance):
    original = instance.horaires
    instance.horaires = original
    assert instance.horaires == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_reviews_setter(instance):
    original = instance.reviews
    instance.reviews = original
    assert instance.reviews == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_numeroTel_setter(instance):
    original = instance.numeroTel
    instance.numeroTel = original
    assert instance.numeroTel == original



@given(instance=Analyse2_Fast_Food_strategy)
def test_analyse2_fast_food_Adresse_setter(instance):
    original = instance.Adresse
    instance.Adresse = original
    assert instance.Adresse == original

@given(instance=Pr_sentation_strategy)
@settings(max_examples=50)
def test_pr_sentation_instantiation(instance):
    assert isinstance(instance, Pr_sentation)



@given(instance=Pr_sentation_strategy)
def test_pr_sentation_numTel_setter(instance):
    original = instance.numTel
    instance.numTel = original
    assert instance.numTel == original



@given(instance=Pr_sentation_strategy)
def test_pr_sentation_adresse_setter(instance):
    original = instance.adresse
    instance.adresse = original
    assert instance.adresse == original



@given(instance=Pr_sentation_strategy)
def test_pr_sentation_ouverture_setter(instance):
    original = instance.ouverture
    instance.ouverture = original
    assert instance.ouverture == original



@given(instance=Pr_sentation_strategy)
def test_pr_sentation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Pr_sentation_strategy)
def test_pr_sentation_siteDeCommande_setter(instance):
    original = instance.siteDeCommande
    instance.siteDeCommande = original
    assert instance.siteDeCommande == original

@given(instance=Photo_strategy)
@settings(max_examples=50)
def test_photo_instantiation(instance):
    assert isinstance(instance, Photo)

@given(instance=Commentaire_strategy)
@settings(max_examples=50)
def test_commentaire_instantiation(instance):
    assert isinstance(instance, Commentaire)



@given(instance=Commentaire_strategy)
def test_commentaire_commentaire_setter(instance):
    original = instance.commentaire
    instance.commentaire = original
    assert instance.commentaire == original



@given(instance=Commentaire_strategy)
def test_commentaire_auteur_setter(instance):
    original = instance.auteur
    instance.auteur = original
    assert instance.auteur == original

@given(instance=AvisGlobal_strategy)
@settings(max_examples=50)
def test_avisglobal_instantiation(instance):
    assert isinstance(instance, AvisGlobal)



@given(instance=AvisGlobal_strategy)
def test_avisglobal_nbAvis_setter(instance):
    original = instance.nbAvis
    instance.nbAvis = original
    assert instance.nbAvis == original



@given(instance=AvisGlobal_strategy)
def test_avisglobal_diagramme_setter(instance):
    original = instance.diagramme
    instance.diagramme = original
    assert instance.diagramme == original



@given(instance=AvisGlobal_strategy)
def test_avisglobal_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original



@given(instance=AvisGlobal_strategy)
def test_avisglobal_Commentaires_setter(instance):
    original = instance.Commentaires
    instance.Commentaires = original
    assert instance.Commentaires == original

@given(instance=FicheRestaurant_strategy)
@settings(max_examples=50)
def test_ficherestaurant_instantiation(instance):
    assert isinstance(instance, FicheRestaurant)



@given(instance=FicheRestaurant_strategy)
def test_ficherestaurant_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=Analyse_Moderateurs_strategy)
@settings(max_examples=50)
def test_analyse_moderateurs_instantiation(instance):
    assert isinstance(instance, Analyse_Moderateurs)

@given(instance=Analyse_Criteres_strategy)
@settings(max_examples=50)
def test_analyse_criteres_instantiation(instance):
    assert isinstance(instance, Analyse_Criteres)



@given(instance=Analyse_Criteres_strategy)
def test_analyse_criteres_respectHoraires_setter(instance):
    original = instance.respectHoraires
    instance.respectHoraires = original
    assert instance.respectHoraires == original



@given(instance=Analyse_Criteres_strategy)
def test_analyse_criteres_rapidite_setter(instance):
    original = instance.rapidite
    instance.rapidite = original
    assert instance.rapidite == original



@given(instance=Analyse_Criteres_strategy)
def test_analyse_criteres_qualit__setter(instance):
    original = instance.qualit_
    instance.qualit_ = original
    assert instance.qualit_ == original



@given(instance=Analyse_Criteres_strategy)
def test_analyse_criteres_rapportQualitePrix_setter(instance):
    original = instance.rapportQualitePrix
    instance.rapportQualitePrix = original
    assert instance.rapportQualitePrix == original



@given(instance=Analyse_Criteres_strategy)
def test_analyse_criteres_amabilite_setter(instance):
    original = instance.amabilite
    instance.amabilite = original
    assert instance.amabilite == original

@given(instance=Analyse_Compte_strategy)
@settings(max_examples=50)
def test_analyse_compte_instantiation(instance):
    assert isinstance(instance, Analyse_Compte)



@given(instance=Analyse_Compte_strategy)
def test_analyse_compte_motdepasse_setter(instance):
    original = instance.motdepasse
    instance.motdepasse = original
    assert instance.motdepasse == original



@given(instance=Analyse_Compte_strategy)
def test_analyse_compte_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original

@given(instance=Analyse_Utilisateur_strategy)
@settings(max_examples=50)
def test_analyse_utilisateur_instantiation(instance):
    assert isinstance(instance, Analyse_Utilisateur)

@given(instance=Analyse_Review_strategy)
@settings(max_examples=50)
def test_analyse_review_instantiation(instance):
    assert isinstance(instance, Analyse_Review)



@given(instance=Analyse_Review_strategy)
def test_analyse_review_lesNotes_setter(instance):
    original = instance.lesNotes
    instance.lesNotes = original
    assert instance.lesNotes == original



@given(instance=Analyse_Review_strategy)
def test_analyse_review_NoteGlobale_setter(instance):
    original = instance.NoteGlobale
    instance.NoteGlobale = original
    assert instance.NoteGlobale == original



@given(instance=Analyse_Review_strategy)
def test_analyse_review_Commentaire_setter(instance):
    original = instance.Commentaire
    instance.Commentaire = original
    assert instance.Commentaire == original

@given(instance=Analyse_Fast_Food_strategy)
@settings(max_examples=50)
def test_analyse_fast_food_instantiation(instance):
    assert isinstance(instance, Analyse_Fast_Food)



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_numeroTel_setter(instance):
    original = instance.numeroTel
    instance.numeroTel = original
    assert instance.numeroTel == original



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_photos_setter(instance):
    original = instance.photos
    instance.photos = original
    assert instance.photos == original



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_prixMax_setter(instance):
    original = instance.prixMax
    instance.prixMax = original
    assert instance.prixMax == original



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_horaires_setter(instance):
    original = instance.horaires
    instance.horaires = original
    assert instance.horaires == original



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_Adresse_setter(instance):
    original = instance.Adresse
    instance.Adresse = original
    assert instance.Adresse == original



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_Ville_setter(instance):
    original = instance.Ville
    instance.Ville = original
    assert instance.Ville == original



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_prixMin_setter(instance):
    original = instance.prixMin
    instance.prixMin = original
    assert instance.prixMin == original



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_nbPlaces_setter(instance):
    original = instance.nbPlaces
    instance.nbPlaces = original
    assert instance.nbPlaces == original



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=Analyse_Fast_Food_strategy)
def test_analyse_fast_food_proprietaire_setter(instance):
    original = instance.proprietaire
    instance.proprietaire = original
    assert instance.proprietaire == original
