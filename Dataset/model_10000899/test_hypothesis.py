import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Admin_add_trajet_UseCase,
    Admin_Passager___conducteur_Actor,
    Admin_s_inscrire_UseCase,
    Admin_UseCase5_UseCase,
    Admin_consulter_trajets_UseCase,
    Admin_suppr_utils_UseCase,
    Admin_modifier_utilis_UseCase,
    Admin_consulter_liste_utilis_UseCase,
    Admin_Admin_Actor,
    covoiturage_Avis,
    covoiturage_Ville,
    covoiturage_Reservations,
    covoiturage_Preferences,
    covoiturage_Voiture,
    covoiturage_Personne,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_admin_add_trajet_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_add_trajet_UseCase)


def test_admin_add_trajet_usecase_constructor_exists():
    assert callable(Admin_add_trajet_UseCase.__init__)


def test_admin_add_trajet_usecase_constructor_args():
    sig = inspect.signature(Admin_add_trajet_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_passager___conducteur_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Passager___conducteur_Actor)


def test_admin_passager___conducteur_actor_constructor_exists():
    assert callable(Admin_Passager___conducteur_Actor.__init__)


def test_admin_passager___conducteur_actor_constructor_args():
    sig = inspect.signature(Admin_Passager___conducteur_Actor.__init__)
    params = list(sig.parameters.keys())



def test_admin_s_inscrire_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_s_inscrire_UseCase)


def test_admin_s_inscrire_usecase_constructor_exists():
    assert callable(Admin_s_inscrire_UseCase.__init__)


def test_admin_s_inscrire_usecase_constructor_args():
    sig = inspect.signature(Admin_s_inscrire_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_usecase5_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_UseCase5_UseCase)


def test_admin_usecase5_usecase_constructor_exists():
    assert callable(Admin_UseCase5_UseCase.__init__)


def test_admin_usecase5_usecase_constructor_args():
    sig = inspect.signature(Admin_UseCase5_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_consulter_trajets_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_consulter_trajets_UseCase)


def test_admin_consulter_trajets_usecase_constructor_exists():
    assert callable(Admin_consulter_trajets_UseCase.__init__)


def test_admin_consulter_trajets_usecase_constructor_args():
    sig = inspect.signature(Admin_consulter_trajets_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_suppr_utils_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_suppr_utils_UseCase)


def test_admin_suppr_utils_usecase_constructor_exists():
    assert callable(Admin_suppr_utils_UseCase.__init__)


def test_admin_suppr_utils_usecase_constructor_args():
    sig = inspect.signature(Admin_suppr_utils_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_modifier_utilis_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_modifier_utilis_UseCase)


def test_admin_modifier_utilis_usecase_constructor_exists():
    assert callable(Admin_modifier_utilis_UseCase.__init__)


def test_admin_modifier_utilis_usecase_constructor_args():
    sig = inspect.signature(Admin_modifier_utilis_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_consulter_liste_utilis_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_consulter_liste_utilis_UseCase)


def test_admin_consulter_liste_utilis_usecase_constructor_exists():
    assert callable(Admin_consulter_liste_utilis_UseCase.__init__)


def test_admin_consulter_liste_utilis_usecase_constructor_args():
    sig = inspect.signature(Admin_consulter_liste_utilis_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Admin_Actor)


def test_admin_admin_actor_constructor_exists():
    assert callable(Admin_Admin_Actor.__init__)


def test_admin_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test_covoiturage_avis_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Avis)


def test_covoiturage_avis_constructor_exists():
    assert callable(covoiturage_Avis.__init__)


def test_covoiturage_avis_constructor_args():
    sig = inspect.signature(covoiturage_Avis.__init__)
    params = list(sig.parameters.keys())
    assert "commentaire" in params, "Missing parameter 'commentaire'"
    assert "id" in params, "Missing parameter 'id'"
    assert "note" in params, "Missing parameter 'note'"

def test_covoiturage_avis_has_commentaire():
    assert hasattr(covoiturage_Avis, "commentaire")
    descriptor = None
    for klass in covoiturage_Avis.__mro__:
        if "commentaire" in klass.__dict__:
            descriptor = klass.__dict__["commentaire"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_avis_has_id():
    assert hasattr(covoiturage_Avis, "id")
    descriptor = None
    for klass in covoiturage_Avis.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_avis_has_note():
    assert hasattr(covoiturage_Avis, "note")
    descriptor = None
    for klass in covoiturage_Avis.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_ville_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Ville)


def test_covoiturage_ville_constructor_exists():
    assert callable(covoiturage_Ville.__init__)


def test_covoiturage_ville_constructor_args():
    sig = inspect.signature(covoiturage_Ville.__init__)
    params = list(sig.parameters.keys())
    assert "cp" in params, "Missing parameter 'cp'"
    assert "id" in params, "Missing parameter 'id'"
    assert "nom" in params, "Missing parameter 'nom'"

def test_covoiturage_ville_has_cp():
    assert hasattr(covoiturage_Ville, "cp")
    descriptor = None
    for klass in covoiturage_Ville.__mro__:
        if "cp" in klass.__dict__:
            descriptor = klass.__dict__["cp"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_ville_has_id():
    assert hasattr(covoiturage_Ville, "id")
    descriptor = None
    for klass in covoiturage_Ville.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_ville_has_nom():
    assert hasattr(covoiturage_Ville, "nom")
    descriptor = None
    for klass in covoiturage_Ville.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_reservations_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Reservations)


def test_covoiturage_reservations_constructor_exists():
    assert callable(covoiturage_Reservations.__init__)


def test_covoiturage_reservations_constructor_args():
    sig = inspect.signature(covoiturage_Reservations.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "date" in params, "Missing parameter 'date'"
    assert "prix" in params, "Missing parameter 'prix'"
    assert "lieuDeDepose" in params, "Missing parameter 'lieuDeDepose'"

def test_covoiturage_reservations_has_id():
    assert hasattr(covoiturage_Reservations, "id")
    descriptor = None
    for klass in covoiturage_Reservations.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_reservations_has_date():
    assert hasattr(covoiturage_Reservations, "date")
    descriptor = None
    for klass in covoiturage_Reservations.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_reservations_has_prix():
    assert hasattr(covoiturage_Reservations, "prix")
    descriptor = None
    for klass in covoiturage_Reservations.__mro__:
        if "prix" in klass.__dict__:
            descriptor = klass.__dict__["prix"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_reservations_has_lieuDeDepose():
    assert hasattr(covoiturage_Reservations, "lieuDeDepose")
    descriptor = None
    for klass in covoiturage_Reservations.__mro__:
        if "lieuDeDepose" in klass.__dict__:
            descriptor = klass.__dict__["lieuDeDepose"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_preferences_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Preferences)


def test_covoiturage_preferences_constructor_exists():
    assert callable(covoiturage_Preferences.__init__)


def test_covoiturage_preferences_constructor_args():
    sig = inspect.signature(covoiturage_Preferences.__init__)
    params = list(sig.parameters.keys())
    assert "valeur" in params, "Missing parameter 'valeur'"
    assert "nomPref" in params, "Missing parameter 'nomPref'"
    assert "id" in params, "Missing parameter 'id'"

def test_covoiturage_preferences_has_valeur():
    assert hasattr(covoiturage_Preferences, "valeur")
    descriptor = None
    for klass in covoiturage_Preferences.__mro__:
        if "valeur" in klass.__dict__:
            descriptor = klass.__dict__["valeur"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_preferences_has_nomPref():
    assert hasattr(covoiturage_Preferences, "nomPref")
    descriptor = None
    for klass in covoiturage_Preferences.__mro__:
        if "nomPref" in klass.__dict__:
            descriptor = klass.__dict__["nomPref"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_preferences_has_id():
    assert hasattr(covoiturage_Preferences, "id")
    descriptor = None
    for klass in covoiturage_Preferences.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_voiture_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Voiture)


def test_covoiturage_voiture_constructor_exists():
    assert callable(covoiturage_Voiture.__init__)


def test_covoiturage_voiture_constructor_args():
    sig = inspect.signature(covoiturage_Voiture.__init__)
    params = list(sig.parameters.keys())
    assert "tabac" in params, "Missing parameter 'tabac'"
    assert "nbPlaces" in params, "Missing parameter 'nbPlaces'"
    assert "model" in params, "Missing parameter 'model'"
    assert "confort" in params, "Missing parameter 'confort'"
    assert "categorie" in params, "Missing parameter 'categorie'"
    assert "id" in params, "Missing parameter 'id'"
    assert "couleur" in params, "Missing parameter 'couleur'"
    assert "marque" in params, "Missing parameter 'marque'"
    assert "climatiseur" in params, "Missing parameter 'climatiseur'"

def test_covoiturage_voiture_has_tabac():
    assert hasattr(covoiturage_Voiture, "tabac")
    descriptor = None
    for klass in covoiturage_Voiture.__mro__:
        if "tabac" in klass.__dict__:
            descriptor = klass.__dict__["tabac"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_nbPlaces():
    assert hasattr(covoiturage_Voiture, "nbPlaces")
    descriptor = None
    for klass in covoiturage_Voiture.__mro__:
        if "nbPlaces" in klass.__dict__:
            descriptor = klass.__dict__["nbPlaces"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_model():
    assert hasattr(covoiturage_Voiture, "model")
    descriptor = None
    for klass in covoiturage_Voiture.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_confort():
    assert hasattr(covoiturage_Voiture, "confort")
    descriptor = None
    for klass in covoiturage_Voiture.__mro__:
        if "confort" in klass.__dict__:
            descriptor = klass.__dict__["confort"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_categorie():
    assert hasattr(covoiturage_Voiture, "categorie")
    descriptor = None
    for klass in covoiturage_Voiture.__mro__:
        if "categorie" in klass.__dict__:
            descriptor = klass.__dict__["categorie"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_id():
    assert hasattr(covoiturage_Voiture, "id")
    descriptor = None
    for klass in covoiturage_Voiture.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_couleur():
    assert hasattr(covoiturage_Voiture, "couleur")
    descriptor = None
    for klass in covoiturage_Voiture.__mro__:
        if "couleur" in klass.__dict__:
            descriptor = klass.__dict__["couleur"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_marque():
    assert hasattr(covoiturage_Voiture, "marque")
    descriptor = None
    for klass in covoiturage_Voiture.__mro__:
        if "marque" in klass.__dict__:
            descriptor = klass.__dict__["marque"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_climatiseur():
    assert hasattr(covoiturage_Voiture, "climatiseur")
    descriptor = None
    for klass in covoiturage_Voiture.__mro__:
        if "climatiseur" in klass.__dict__:
            descriptor = klass.__dict__["climatiseur"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_personne_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Personne)


def test_covoiturage_personne_constructor_exists():
    assert callable(covoiturage_Personne.__init__)


def test_covoiturage_personne_constructor_args():
    sig = inspect.signature(covoiturage_Personne.__init__)
    params = list(sig.parameters.keys())
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "tel" in params, "Missing parameter 'tel'"
    assert "id" in params, "Missing parameter 'id'"
    assert "mail" in params, "Missing parameter 'mail'"

def test_covoiturage_personne_has_prenom():
    assert hasattr(covoiturage_Personne, "prenom")
    descriptor = None
    for klass in covoiturage_Personne.__mro__:
        if "prenom" in klass.__dict__:
            descriptor = klass.__dict__["prenom"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_personne_has_nom():
    assert hasattr(covoiturage_Personne, "nom")
    descriptor = None
    for klass in covoiturage_Personne.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_personne_has_tel():
    assert hasattr(covoiturage_Personne, "tel")
    descriptor = None
    for klass in covoiturage_Personne.__mro__:
        if "tel" in klass.__dict__:
            descriptor = klass.__dict__["tel"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_personne_has_id():
    assert hasattr(covoiturage_Personne, "id")
    descriptor = None
    for klass in covoiturage_Personne.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_personne_has_mail():
    assert hasattr(covoiturage_Personne, "mail")
    descriptor = None
    for klass in covoiturage_Personne.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
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
Admin_add_trajet_UseCase_strategy = st.builds(
    Admin_add_trajet_UseCase,
)
Admin_Passager___conducteur_Actor_strategy = st.builds(
    Admin_Passager___conducteur_Actor,
)
Admin_s_inscrire_UseCase_strategy = st.builds(
    Admin_s_inscrire_UseCase,
)
Admin_UseCase5_UseCase_strategy = st.builds(
    Admin_UseCase5_UseCase,
)
Admin_consulter_trajets_UseCase_strategy = st.builds(
    Admin_consulter_trajets_UseCase,
)
Admin_suppr_utils_UseCase_strategy = st.builds(
    Admin_suppr_utils_UseCase,
)
Admin_modifier_utilis_UseCase_strategy = st.builds(
    Admin_modifier_utilis_UseCase,
)
Admin_consulter_liste_utilis_UseCase_strategy = st.builds(
    Admin_consulter_liste_utilis_UseCase,
)
Admin_Admin_Actor_strategy = st.builds(
    Admin_Admin_Actor,
)
covoiturage_Avis_strategy = st.builds(
    covoiturage_Avis,
    commentaire=
        safe_text,
    id=
        st.integers(),
    note=
        st.integers()
)
covoiturage_Ville_strategy = st.builds(
    covoiturage_Ville,
    cp=
        safe_text,
    id=
        st.integers(),
    nom=
        safe_text
)
covoiturage_Reservations_strategy = st.builds(
    covoiturage_Reservations,
    id=
        st.integers(),
    date=
        st.dates(),
    prix=
        st.integers(),
    lieuDeDepose=
        safe_text
)
covoiturage_Preferences_strategy = st.builds(
    covoiturage_Preferences,
    valeur=
        safe_text,
    nomPref=
        safe_text,
    id=
        st.integers()
)
covoiturage_Voiture_strategy = st.builds(
    covoiturage_Voiture,
    tabac=
        st.booleans(),
    nbPlaces=
        st.integers(),
    model=
        safe_text,
    confort=
        safe_text,
    categorie=
        safe_text,
    id=
        st.integers(),
    couleur=
        safe_text,
    marque=
        safe_text,
    climatiseur=
        st.booleans()
)
covoiturage_Personne_strategy = st.builds(
    covoiturage_Personne,
    prenom=
        safe_text,
    nom=
        safe_text,
    tel=
        safe_text,
    id=
        st.integers(),
    mail=
        safe_text
)

@given(instance=Admin_add_trajet_UseCase_strategy)
@settings(max_examples=50)
def test_admin_add_trajet_usecase_instantiation(instance):
    assert isinstance(instance, Admin_add_trajet_UseCase)

@given(instance=Admin_Passager___conducteur_Actor_strategy)
@settings(max_examples=50)
def test_admin_passager___conducteur_actor_instantiation(instance):
    assert isinstance(instance, Admin_Passager___conducteur_Actor)

@given(instance=Admin_s_inscrire_UseCase_strategy)
@settings(max_examples=50)
def test_admin_s_inscrire_usecase_instantiation(instance):
    assert isinstance(instance, Admin_s_inscrire_UseCase)

@given(instance=Admin_UseCase5_UseCase_strategy)
@settings(max_examples=50)
def test_admin_usecase5_usecase_instantiation(instance):
    assert isinstance(instance, Admin_UseCase5_UseCase)

@given(instance=Admin_consulter_trajets_UseCase_strategy)
@settings(max_examples=50)
def test_admin_consulter_trajets_usecase_instantiation(instance):
    assert isinstance(instance, Admin_consulter_trajets_UseCase)

@given(instance=Admin_suppr_utils_UseCase_strategy)
@settings(max_examples=50)
def test_admin_suppr_utils_usecase_instantiation(instance):
    assert isinstance(instance, Admin_suppr_utils_UseCase)

@given(instance=Admin_modifier_utilis_UseCase_strategy)
@settings(max_examples=50)
def test_admin_modifier_utilis_usecase_instantiation(instance):
    assert isinstance(instance, Admin_modifier_utilis_UseCase)

@given(instance=Admin_consulter_liste_utilis_UseCase_strategy)
@settings(max_examples=50)
def test_admin_consulter_liste_utilis_usecase_instantiation(instance):
    assert isinstance(instance, Admin_consulter_liste_utilis_UseCase)

@given(instance=Admin_Admin_Actor_strategy)
@settings(max_examples=50)
def test_admin_admin_actor_instantiation(instance):
    assert isinstance(instance, Admin_Admin_Actor)

@given(instance=covoiturage_Avis_strategy)
@settings(max_examples=50)
def test_covoiturage_avis_instantiation(instance):
    assert isinstance(instance, covoiturage_Avis)



@given(instance=covoiturage_Avis_strategy)
def test_covoiturage_avis_commentaire_setter(instance):
    original = instance.commentaire
    instance.commentaire = original
    assert instance.commentaire == original



@given(instance=covoiturage_Avis_strategy)
def test_covoiturage_avis_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=covoiturage_Avis_strategy)
def test_covoiturage_avis_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=covoiturage_Ville_strategy)
@settings(max_examples=50)
def test_covoiturage_ville_instantiation(instance):
    assert isinstance(instance, covoiturage_Ville)



@given(instance=covoiturage_Ville_strategy)
def test_covoiturage_ville_cp_setter(instance):
    original = instance.cp
    instance.cp = original
    assert instance.cp == original



@given(instance=covoiturage_Ville_strategy)
def test_covoiturage_ville_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=covoiturage_Ville_strategy)
def test_covoiturage_ville_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=covoiturage_Reservations_strategy)
@settings(max_examples=50)
def test_covoiturage_reservations_instantiation(instance):
    assert isinstance(instance, covoiturage_Reservations)



@given(instance=covoiturage_Reservations_strategy)
def test_covoiturage_reservations_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=covoiturage_Reservations_strategy)
def test_covoiturage_reservations_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=covoiturage_Reservations_strategy)
def test_covoiturage_reservations_prix_setter(instance):
    original = instance.prix
    instance.prix = original
    assert instance.prix == original



@given(instance=covoiturage_Reservations_strategy)
def test_covoiturage_reservations_lieuDeDepose_setter(instance):
    original = instance.lieuDeDepose
    instance.lieuDeDepose = original
    assert instance.lieuDeDepose == original

@given(instance=covoiturage_Preferences_strategy)
@settings(max_examples=50)
def test_covoiturage_preferences_instantiation(instance):
    assert isinstance(instance, covoiturage_Preferences)



@given(instance=covoiturage_Preferences_strategy)
def test_covoiturage_preferences_valeur_setter(instance):
    original = instance.valeur
    instance.valeur = original
    assert instance.valeur == original



@given(instance=covoiturage_Preferences_strategy)
def test_covoiturage_preferences_nomPref_setter(instance):
    original = instance.nomPref
    instance.nomPref = original
    assert instance.nomPref == original



@given(instance=covoiturage_Preferences_strategy)
def test_covoiturage_preferences_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=covoiturage_Voiture_strategy)
@settings(max_examples=50)
def test_covoiturage_voiture_instantiation(instance):
    assert isinstance(instance, covoiturage_Voiture)



@given(instance=covoiturage_Voiture_strategy)
def test_covoiturage_voiture_tabac_setter(instance):
    original = instance.tabac
    instance.tabac = original
    assert instance.tabac == original



@given(instance=covoiturage_Voiture_strategy)
def test_covoiturage_voiture_nbPlaces_setter(instance):
    original = instance.nbPlaces
    instance.nbPlaces = original
    assert instance.nbPlaces == original



@given(instance=covoiturage_Voiture_strategy)
def test_covoiturage_voiture_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=covoiturage_Voiture_strategy)
def test_covoiturage_voiture_confort_setter(instance):
    original = instance.confort
    instance.confort = original
    assert instance.confort == original



@given(instance=covoiturage_Voiture_strategy)
def test_covoiturage_voiture_categorie_setter(instance):
    original = instance.categorie
    instance.categorie = original
    assert instance.categorie == original



@given(instance=covoiturage_Voiture_strategy)
def test_covoiturage_voiture_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=covoiturage_Voiture_strategy)
def test_covoiturage_voiture_couleur_setter(instance):
    original = instance.couleur
    instance.couleur = original
    assert instance.couleur == original



@given(instance=covoiturage_Voiture_strategy)
def test_covoiturage_voiture_marque_setter(instance):
    original = instance.marque
    instance.marque = original
    assert instance.marque == original



@given(instance=covoiturage_Voiture_strategy)
def test_covoiturage_voiture_climatiseur_setter(instance):
    original = instance.climatiseur
    instance.climatiseur = original
    assert instance.climatiseur == original

@given(instance=covoiturage_Personne_strategy)
@settings(max_examples=50)
def test_covoiturage_personne_instantiation(instance):
    assert isinstance(instance, covoiturage_Personne)



@given(instance=covoiturage_Personne_strategy)
def test_covoiturage_personne_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=covoiturage_Personne_strategy)
def test_covoiturage_personne_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=covoiturage_Personne_strategy)
def test_covoiturage_personne_tel_setter(instance):
    original = instance.tel
    instance.tel = original
    assert instance.tel == original



@given(instance=covoiturage_Personne_strategy)
def test_covoiturage_personne_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=covoiturage_Personne_strategy)
def test_covoiturage_personne_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original
