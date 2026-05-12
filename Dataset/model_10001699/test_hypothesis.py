import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    domain_Reservation,
    domain_Avis,
    domain_Ville,
    domain_Trajet,
    domain_Authentification,
    domain_Voiture,
    domain_Profil,
    domain_Role,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_domain_reservation_is_not_abstract():
    assert not inspect.isabstract(domain_Reservation)


def test_domain_reservation_constructor_exists():
    assert callable(domain_Reservation.__init__)


def test_domain_reservation_constructor_args():
    sig = inspect.signature(domain_Reservation.__init__)
    params = list(sig.parameters.keys())
    assert "dateReservation" in params, "Missing parameter 'dateReservation'"
    assert "id" in params, "Missing parameter 'id'"
    assert "id2" in params, "Missing parameter 'id2'"

def test_domain_reservation_has_dateReservation():
    assert hasattr(domain_Reservation, "dateReservation")
    descriptor = None
    for klass in domain_Reservation.__mro__:
        if "dateReservation" in klass.__dict__:
            descriptor = klass.__dict__["dateReservation"]
            break
    assert isinstance(descriptor, property)

def test_domain_reservation_has_id():
    assert hasattr(domain_Reservation, "id")
    descriptor = None
    for klass in domain_Reservation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_domain_reservation_has_id2():
    assert hasattr(domain_Reservation, "id2")
    descriptor = None
    for klass in domain_Reservation.__mro__:
        if "id2" in klass.__dict__:
            descriptor = klass.__dict__["id2"]
            break
    assert isinstance(descriptor, property)



def test_domain_avis_is_not_abstract():
    assert not inspect.isabstract(domain_Avis)


def test_domain_avis_constructor_exists():
    assert callable(domain_Avis.__init__)


def test_domain_avis_constructor_args():
    sig = inspect.signature(domain_Avis.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "commentaire" in params, "Missing parameter 'commentaire'"
    assert "note" in params, "Missing parameter 'note'"

def test_domain_avis_has_id():
    assert hasattr(domain_Avis, "id")
    descriptor = None
    for klass in domain_Avis.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_domain_avis_has_commentaire():
    assert hasattr(domain_Avis, "commentaire")
    descriptor = None
    for klass in domain_Avis.__mro__:
        if "commentaire" in klass.__dict__:
            descriptor = klass.__dict__["commentaire"]
            break
    assert isinstance(descriptor, property)

def test_domain_avis_has_note():
    assert hasattr(domain_Avis, "note")
    descriptor = None
    for klass in domain_Avis.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_domain_ville_is_not_abstract():
    assert not inspect.isabstract(domain_Ville)


def test_domain_ville_constructor_exists():
    assert callable(domain_Ville.__init__)


def test_domain_ville_constructor_args():
    sig = inspect.signature(domain_Ville.__init__)
    params = list(sig.parameters.keys())
    assert "cp" in params, "Missing parameter 'cp'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "id" in params, "Missing parameter 'id'"

def test_domain_ville_has_cp():
    assert hasattr(domain_Ville, "cp")
    descriptor = None
    for klass in domain_Ville.__mro__:
        if "cp" in klass.__dict__:
            descriptor = klass.__dict__["cp"]
            break
    assert isinstance(descriptor, property)

def test_domain_ville_has_nom():
    assert hasattr(domain_Ville, "nom")
    descriptor = None
    for klass in domain_Ville.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_domain_ville_has_id():
    assert hasattr(domain_Ville, "id")
    descriptor = None
    for klass in domain_Ville.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_domain_trajet_is_not_abstract():
    assert not inspect.isabstract(domain_Trajet)


def test_domain_trajet_constructor_exists():
    assert callable(domain_Trajet.__init__)


def test_domain_trajet_constructor_args():
    sig = inspect.signature(domain_Trajet.__init__)
    params = list(sig.parameters.keys())
    assert "depart" in params, "Missing parameter 'depart'"
    assert "prix" in params, "Missing parameter 'prix'"
    assert "date" in params, "Missing parameter 'date'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "id" in params, "Missing parameter 'id'"

def test_domain_trajet_has_depart():
    assert hasattr(domain_Trajet, "depart")
    descriptor = None
    for klass in domain_Trajet.__mro__:
        if "depart" in klass.__dict__:
            descriptor = klass.__dict__["depart"]
            break
    assert isinstance(descriptor, property)

def test_domain_trajet_has_prix():
    assert hasattr(domain_Trajet, "prix")
    descriptor = None
    for klass in domain_Trajet.__mro__:
        if "prix" in klass.__dict__:
            descriptor = klass.__dict__["prix"]
            break
    assert isinstance(descriptor, property)

def test_domain_trajet_has_date():
    assert hasattr(domain_Trajet, "date")
    descriptor = None
    for klass in domain_Trajet.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_domain_trajet_has_destination():
    assert hasattr(domain_Trajet, "destination")
    descriptor = None
    for klass in domain_Trajet.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_domain_trajet_has_id():
    assert hasattr(domain_Trajet, "id")
    descriptor = None
    for klass in domain_Trajet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_domain_authentification_is_not_abstract():
    assert not inspect.isabstract(domain_Authentification)


def test_domain_authentification_constructor_exists():
    assert callable(domain_Authentification.__init__)


def test_domain_authentification_constructor_args():
    sig = inspect.signature(domain_Authentification.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"

def test_domain_authentification_has_id():
    assert hasattr(domain_Authentification, "id")
    descriptor = None
    for klass in domain_Authentification.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_domain_authentification_has_password():
    assert hasattr(domain_Authentification, "password")
    descriptor = None
    for klass in domain_Authentification.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_domain_voiture_is_not_abstract():
    assert not inspect.isabstract(domain_Voiture)


def test_domain_voiture_constructor_exists():
    assert callable(domain_Voiture.__init__)


def test_domain_voiture_constructor_args():
    sig = inspect.signature(domain_Voiture.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "model" in params, "Missing parameter 'model'"
    assert "categorie" in params, "Missing parameter 'categorie'"
    assert "marque" in params, "Missing parameter 'marque'"
    assert "confort" in params, "Missing parameter 'confort'"
    assert "nbPlaces" in params, "Missing parameter 'nbPlaces'"

def test_domain_voiture_has_id():
    assert hasattr(domain_Voiture, "id")
    descriptor = None
    for klass in domain_Voiture.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_domain_voiture_has_model():
    assert hasattr(domain_Voiture, "model")
    descriptor = None
    for klass in domain_Voiture.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_domain_voiture_has_categorie():
    assert hasattr(domain_Voiture, "categorie")
    descriptor = None
    for klass in domain_Voiture.__mro__:
        if "categorie" in klass.__dict__:
            descriptor = klass.__dict__["categorie"]
            break
    assert isinstance(descriptor, property)

def test_domain_voiture_has_marque():
    assert hasattr(domain_Voiture, "marque")
    descriptor = None
    for klass in domain_Voiture.__mro__:
        if "marque" in klass.__dict__:
            descriptor = klass.__dict__["marque"]
            break
    assert isinstance(descriptor, property)

def test_domain_voiture_has_confort():
    assert hasattr(domain_Voiture, "confort")
    descriptor = None
    for klass in domain_Voiture.__mro__:
        if "confort" in klass.__dict__:
            descriptor = klass.__dict__["confort"]
            break
    assert isinstance(descriptor, property)

def test_domain_voiture_has_nbPlaces():
    assert hasattr(domain_Voiture, "nbPlaces")
    descriptor = None
    for klass in domain_Voiture.__mro__:
        if "nbPlaces" in klass.__dict__:
            descriptor = klass.__dict__["nbPlaces"]
            break
    assert isinstance(descriptor, property)



def test_domain_profil_is_not_abstract():
    assert not inspect.isabstract(domain_Profil)


def test_domain_profil_constructor_exists():
    assert callable(domain_Profil.__init__)


def test_domain_profil_constructor_args():
    sig = inspect.signature(domain_Profil.__init__)
    params = list(sig.parameters.keys())
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "mail" in params, "Missing parameter 'mail'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "id" in params, "Missing parameter 'id'"
    assert "role" in params, "Missing parameter 'role'"
    assert "tel" in params, "Missing parameter 'tel'"

def test_domain_profil_has_prenom():
    assert hasattr(domain_Profil, "prenom")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "prenom" in klass.__dict__:
            descriptor = klass.__dict__["prenom"]
            break
    assert isinstance(descriptor, property)

def test_domain_profil_has_mail():
    assert hasattr(domain_Profil, "mail")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
            break
    assert isinstance(descriptor, property)

def test_domain_profil_has_nom():
    assert hasattr(domain_Profil, "nom")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_domain_profil_has_id():
    assert hasattr(domain_Profil, "id")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_domain_profil_has_role():
    assert hasattr(domain_Profil, "role")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_domain_profil_has_tel():
    assert hasattr(domain_Profil, "tel")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "tel" in klass.__dict__:
            descriptor = klass.__dict__["tel"]
            break
    assert isinstance(descriptor, property)

def test_domain_role_exists():
    # Check that the Enumeration exists
    assert domain_Role is not None

def test_domain_role_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in domain_Role]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in domain_Role"


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
domain_Reservation_strategy = st.builds(
    domain_Reservation,
    dateReservation=
        st.dates(),
    id=
        st.integers(),
    id2=
        st.integers()
)
domain_Avis_strategy = st.builds(
    domain_Avis,
    id=
        st.integers(),
    commentaire=
        safe_text,
    note=
        st.integers()
)
domain_Ville_strategy = st.builds(
    domain_Ville,
    cp=
        st.integers(),
    nom=
        safe_text,
    id=
        st.integers()
)
domain_Trajet_strategy = st.builds(
    domain_Trajet,
    depart=
        st.none(),
    prix=
        st.integers(),
    date=
        st.dates(),
    destination=
        st.none(),
    id=
        st.integers()
)
domain_Authentification_strategy = st.builds(
    domain_Authentification,
    id=
        safe_text,
    password=
        safe_text
)
domain_Voiture_strategy = st.builds(
    domain_Voiture,
    id=
        st.integers(),
    model=
        safe_text,
    categorie=
        safe_text,
    marque=
        safe_text,
    confort=
        safe_text,
    nbPlaces=
        st.integers()
)
domain_Profil_strategy = st.builds(
    domain_Profil,
    prenom=
        safe_text,
    mail=
        safe_text,
    nom=
        safe_text,
    id=
        st.integers(),
    role=
        st.none(),
    tel=
        safe_text
)

@given(instance=domain_Reservation_strategy)
@settings(max_examples=50)
def test_domain_reservation_instantiation(instance):
    assert isinstance(instance, domain_Reservation)



@given(instance=domain_Reservation_strategy)
def test_domain_reservation_dateReservation_setter(instance):
    original = instance.dateReservation
    instance.dateReservation = original
    assert instance.dateReservation == original



@given(instance=domain_Reservation_strategy)
def test_domain_reservation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=domain_Reservation_strategy)
def test_domain_reservation_id2_setter(instance):
    original = instance.id2
    instance.id2 = original
    assert instance.id2 == original

@given(instance=domain_Avis_strategy)
@settings(max_examples=50)
def test_domain_avis_instantiation(instance):
    assert isinstance(instance, domain_Avis)



@given(instance=domain_Avis_strategy)
def test_domain_avis_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=domain_Avis_strategy)
def test_domain_avis_commentaire_setter(instance):
    original = instance.commentaire
    instance.commentaire = original
    assert instance.commentaire == original



@given(instance=domain_Avis_strategy)
def test_domain_avis_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=domain_Ville_strategy)
@settings(max_examples=50)
def test_domain_ville_instantiation(instance):
    assert isinstance(instance, domain_Ville)



@given(instance=domain_Ville_strategy)
def test_domain_ville_cp_setter(instance):
    original = instance.cp
    instance.cp = original
    assert instance.cp == original



@given(instance=domain_Ville_strategy)
def test_domain_ville_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=domain_Ville_strategy)
def test_domain_ville_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=domain_Trajet_strategy)
@settings(max_examples=50)
def test_domain_trajet_instantiation(instance):
    assert isinstance(instance, domain_Trajet)



@given(instance=domain_Trajet_strategy)
def test_domain_trajet_depart_setter(instance):
    original = instance.depart
    instance.depart = original
    assert instance.depart == original



@given(instance=domain_Trajet_strategy)
def test_domain_trajet_prix_setter(instance):
    original = instance.prix
    instance.prix = original
    assert instance.prix == original



@given(instance=domain_Trajet_strategy)
def test_domain_trajet_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=domain_Trajet_strategy)
def test_domain_trajet_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=domain_Trajet_strategy)
def test_domain_trajet_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=domain_Authentification_strategy)
@settings(max_examples=50)
def test_domain_authentification_instantiation(instance):
    assert isinstance(instance, domain_Authentification)



@given(instance=domain_Authentification_strategy)
def test_domain_authentification_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=domain_Authentification_strategy)
def test_domain_authentification_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=domain_Voiture_strategy)
@settings(max_examples=50)
def test_domain_voiture_instantiation(instance):
    assert isinstance(instance, domain_Voiture)



@given(instance=domain_Voiture_strategy)
def test_domain_voiture_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=domain_Voiture_strategy)
def test_domain_voiture_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=domain_Voiture_strategy)
def test_domain_voiture_categorie_setter(instance):
    original = instance.categorie
    instance.categorie = original
    assert instance.categorie == original



@given(instance=domain_Voiture_strategy)
def test_domain_voiture_marque_setter(instance):
    original = instance.marque
    instance.marque = original
    assert instance.marque == original



@given(instance=domain_Voiture_strategy)
def test_domain_voiture_confort_setter(instance):
    original = instance.confort
    instance.confort = original
    assert instance.confort == original



@given(instance=domain_Voiture_strategy)
def test_domain_voiture_nbPlaces_setter(instance):
    original = instance.nbPlaces
    instance.nbPlaces = original
    assert instance.nbPlaces == original

@given(instance=domain_Profil_strategy)
@settings(max_examples=50)
def test_domain_profil_instantiation(instance):
    assert isinstance(instance, domain_Profil)



@given(instance=domain_Profil_strategy)
def test_domain_profil_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=domain_Profil_strategy)
def test_domain_profil_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original



@given(instance=domain_Profil_strategy)
def test_domain_profil_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=domain_Profil_strategy)
def test_domain_profil_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=domain_Profil_strategy)
def test_domain_profil_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=domain_Profil_strategy)
def test_domain_profil_tel_setter(instance):
    original = instance.tel
    instance.tel = original
    assert instance.tel == original
