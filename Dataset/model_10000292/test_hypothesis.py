import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Trajet1,
    Trajet,
    Voiture,
    Avis1,
    Utilisateur,
    Avis,
    Personne,
    Class,
    Chemin_Interface,
    Passager,
    Conducteur,
    Lieu,
    V_hicule,
    Utilisateur1,
    Personne2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trajet1_is_not_abstract():
    assert not inspect.isabstract(Trajet1)


def test_trajet1_constructor_exists():
    assert callable(Trajet1.__init__)


def test_trajet1_constructor_args():
    sig = inspect.signature(Trajet1.__init__)
    params = list(sig.parameters.keys())
    assert "dateFin" in params, "Missing parameter 'dateFin'"
    assert "lieudebut" in params, "Missing parameter 'lieudebut'"
    assert "datedebut" in params, "Missing parameter 'datedebut'"
    assert "lieuFin" in params, "Missing parameter 'lieuFin'"

def test_trajet1_has_dateFin():
    assert hasattr(Trajet1, "dateFin")
    descriptor = None
    for klass in Trajet1.__mro__:
        if "dateFin" in klass.__dict__:
            descriptor = klass.__dict__["dateFin"]
            break
    assert isinstance(descriptor, property)

def test_trajet1_has_lieudebut():
    assert hasattr(Trajet1, "lieudebut")
    descriptor = None
    for klass in Trajet1.__mro__:
        if "lieudebut" in klass.__dict__:
            descriptor = klass.__dict__["lieudebut"]
            break
    assert isinstance(descriptor, property)

def test_trajet1_has_datedebut():
    assert hasattr(Trajet1, "datedebut")
    descriptor = None
    for klass in Trajet1.__mro__:
        if "datedebut" in klass.__dict__:
            descriptor = klass.__dict__["datedebut"]
            break
    assert isinstance(descriptor, property)

def test_trajet1_has_lieuFin():
    assert hasattr(Trajet1, "lieuFin")
    descriptor = None
    for klass in Trajet1.__mro__:
        if "lieuFin" in klass.__dict__:
            descriptor = klass.__dict__["lieuFin"]
            break
    assert isinstance(descriptor, property)



def test_trajet_is_not_abstract():
    assert not inspect.isabstract(Trajet)


def test_trajet_constructor_exists():
    assert callable(Trajet.__init__)


def test_trajet_constructor_args():
    sig = inspect.signature(Trajet.__init__)
    params = list(sig.parameters.keys())
    assert "prix" in params, "Missing parameter 'prix'"
    assert "placesRestantes" in params, "Missing parameter 'placesRestantes'"
    assert "depart" in params, "Missing parameter 'depart'"
    assert "date" in params, "Missing parameter 'date'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "description" in params, "Missing parameter 'description'"

def test_trajet_has_prix():
    assert hasattr(Trajet, "prix")
    descriptor = None
    for klass in Trajet.__mro__:
        if "prix" in klass.__dict__:
            descriptor = klass.__dict__["prix"]
            break
    assert isinstance(descriptor, property)

def test_trajet_has_placesRestantes():
    assert hasattr(Trajet, "placesRestantes")
    descriptor = None
    for klass in Trajet.__mro__:
        if "placesRestantes" in klass.__dict__:
            descriptor = klass.__dict__["placesRestantes"]
            break
    assert isinstance(descriptor, property)

def test_trajet_has_depart():
    assert hasattr(Trajet, "depart")
    descriptor = None
    for klass in Trajet.__mro__:
        if "depart" in klass.__dict__:
            descriptor = klass.__dict__["depart"]
            break
    assert isinstance(descriptor, property)

def test_trajet_has_date():
    assert hasattr(Trajet, "date")
    descriptor = None
    for klass in Trajet.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_trajet_has_destination():
    assert hasattr(Trajet, "destination")
    descriptor = None
    for klass in Trajet.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_trajet_has_description():
    assert hasattr(Trajet, "description")
    descriptor = None
    for klass in Trajet.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_voiture_is_not_abstract():
    assert not inspect.isabstract(Voiture)


def test_voiture_constructor_exists():
    assert callable(Voiture.__init__)


def test_voiture_constructor_args():
    sig = inspect.signature(Voiture.__init__)
    params = list(sig.parameters.keys())
    assert "places" in params, "Missing parameter 'places'"

def test_voiture_has_places():
    assert hasattr(Voiture, "places")
    descriptor = None
    for klass in Voiture.__mro__:
        if "places" in klass.__dict__:
            descriptor = klass.__dict__["places"]
            break
    assert isinstance(descriptor, property)



def test_avis1_is_not_abstract():
    assert not inspect.isabstract(Avis1)


def test_avis1_constructor_exists():
    assert callable(Avis1.__init__)


def test_avis1_constructor_args():
    sig = inspect.signature(Avis1.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "note" in params, "Missing parameter 'note'"

def test_avis1_has_description():
    assert hasattr(Avis1, "description")
    descriptor = None
    for klass in Avis1.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_avis1_has_note():
    assert hasattr(Avis1, "note")
    descriptor = None
    for klass in Avis1.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_utilisateur_is_not_abstract():
    assert not inspect.isabstract(Utilisateur)


def test_utilisateur_constructor_exists():
    assert callable(Utilisateur.__init__)


def test_utilisateur_constructor_args():
    sig = inspect.signature(Utilisateur.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "photoDeProfil" in params, "Missing parameter 'photoDeProfil'"
    assert "score" in params, "Missing parameter 'score'"
    assert "nbAvis" in params, "Missing parameter 'nbAvis'"

def test_utilisateur_has_nom():
    assert hasattr(Utilisateur, "nom")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_photoDeProfil():
    assert hasattr(Utilisateur, "photoDeProfil")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "photoDeProfil" in klass.__dict__:
            descriptor = klass.__dict__["photoDeProfil"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_score():
    assert hasattr(Utilisateur, "score")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_nbAvis():
    assert hasattr(Utilisateur, "nbAvis")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "nbAvis" in klass.__dict__:
            descriptor = klass.__dict__["nbAvis"]
            break
    assert isinstance(descriptor, property)



def test_avis_is_not_abstract():
    assert not inspect.isabstract(Avis)


def test_avis_constructor_exists():
    assert callable(Avis.__init__)


def test_avis_constructor_args():
    sig = inspect.signature(Avis.__init__)
    params = list(sig.parameters.keys())



def test_personne_is_not_abstract():
    assert not inspect.isabstract(Personne)


def test_personne_constructor_exists():
    assert callable(Personne.__init__)


def test_personne_constructor_args():
    sig = inspect.signature(Personne.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_chemin_interface_is_not_abstract():
    assert not inspect.isabstract(Chemin_Interface)


def test_chemin_interface_constructor_exists():
    assert callable(Chemin_Interface.__init__)


def test_chemin_interface_constructor_args():
    sig = inspect.signature(Chemin_Interface.__init__)
    params = list(sig.parameters.keys())



def test_passager_is_not_abstract():
    assert not inspect.isabstract(Passager)


def test_passager_constructor_exists():
    assert callable(Passager.__init__)


def test_passager_constructor_args():
    sig = inspect.signature(Passager.__init__)
    params = list(sig.parameters.keys())



def test_conducteur_is_not_abstract():
    assert not inspect.isabstract(Conducteur)


def test_conducteur_constructor_exists():
    assert callable(Conducteur.__init__)


def test_conducteur_constructor_args():
    sig = inspect.signature(Conducteur.__init__)
    params = list(sig.parameters.keys())



def test_lieu_is_not_abstract():
    assert not inspect.isabstract(Lieu)


def test_lieu_constructor_exists():
    assert callable(Lieu.__init__)


def test_lieu_constructor_args():
    sig = inspect.signature(Lieu.__init__)
    params = list(sig.parameters.keys())



def test_v_hicule_is_not_abstract():
    assert not inspect.isabstract(V_hicule)


def test_v_hicule_constructor_exists():
    assert callable(V_hicule.__init__)


def test_v_hicule_constructor_args():
    sig = inspect.signature(V_hicule.__init__)
    params = list(sig.parameters.keys())
    assert "propri_taire" in params, "Missing parameter 'propri_taire'"
    assert "modele" in params, "Missing parameter 'modele'"
    assert "marque" in params, "Missing parameter 'marque'"
    assert "imatriculation" in params, "Missing parameter 'imatriculation'"

def test_v_hicule_has_propri_taire():
    assert hasattr(V_hicule, "propri_taire")
    descriptor = None
    for klass in V_hicule.__mro__:
        if "propri_taire" in klass.__dict__:
            descriptor = klass.__dict__["propri_taire"]
            break
    assert isinstance(descriptor, property)

def test_v_hicule_has_modele():
    assert hasattr(V_hicule, "modele")
    descriptor = None
    for klass in V_hicule.__mro__:
        if "modele" in klass.__dict__:
            descriptor = klass.__dict__["modele"]
            break
    assert isinstance(descriptor, property)

def test_v_hicule_has_marque():
    assert hasattr(V_hicule, "marque")
    descriptor = None
    for klass in V_hicule.__mro__:
        if "marque" in klass.__dict__:
            descriptor = klass.__dict__["marque"]
            break
    assert isinstance(descriptor, property)

def test_v_hicule_has_imatriculation():
    assert hasattr(V_hicule, "imatriculation")
    descriptor = None
    for klass in V_hicule.__mro__:
        if "imatriculation" in klass.__dict__:
            descriptor = klass.__dict__["imatriculation"]
            break
    assert isinstance(descriptor, property)



def test_utilisateur1_is_not_abstract():
    assert not inspect.isabstract(Utilisateur1)


def test_utilisateur1_constructor_exists():
    assert callable(Utilisateur1.__init__)


def test_utilisateur1_constructor_args():
    sig = inspect.signature(Utilisateur1.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "adresse" in params, "Missing parameter 'adresse'"

def test_utilisateur1_has_age():
    assert hasattr(Utilisateur1, "age")
    descriptor = None
    for klass in Utilisateur1.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur1_has_nom():
    assert hasattr(Utilisateur1, "nom")
    descriptor = None
    for klass in Utilisateur1.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur1_has_adresse():
    assert hasattr(Utilisateur1, "adresse")
    descriptor = None
    for klass in Utilisateur1.__mro__:
        if "adresse" in klass.__dict__:
            descriptor = klass.__dict__["adresse"]
            break
    assert isinstance(descriptor, property)

def test_personne2_exists():
    # Check that the Enumeration exists
    assert Personne2 is not None

def test_personne2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Personne2]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Personne2"


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
Trajet1_strategy = st.builds(
    Trajet1,
    dateFin=
        safe_text,
    lieudebut=
        st.none(),
    datedebut=
        safe_text,
    lieuFin=
        st.none()
)
Trajet_strategy = st.builds(
    Trajet,
    prix=
        st.integers(),
    placesRestantes=
        st.integers(),
    depart=
        st.none(),
    date=
        safe_text,
    destination=
        st.none(),
    description=
        safe_text
)
Voiture_strategy = st.builds(
    Voiture,
    places=
        st.integers()
)
Avis1_strategy = st.builds(
    Avis1,
    description=
        safe_text,
    note=
        st.integers()
)
Utilisateur_strategy = st.builds(
    Utilisateur,
    nom=
        safe_text,
    photoDeProfil=
        safe_text,
    score=
        safe_text,
    nbAvis=
        st.integers()
)
Avis_strategy = st.builds(
    Avis,
)
Personne_strategy = st.builds(
    Personne,
)
Class_strategy = st.builds(
    Class,
)
Chemin_Interface_strategy = st.builds(
    Chemin_Interface,
)
Passager_strategy = st.builds(
    Passager,
)
Conducteur_strategy = st.builds(
    Conducteur,
)
Lieu_strategy = st.builds(
    Lieu,
)
V_hicule_strategy = st.builds(
    V_hicule,
    propri_taire=
        st.none(),
    modele=
        safe_text,
    marque=
        safe_text,
    imatriculation=
        safe_text
)
Utilisateur1_strategy = st.builds(
    Utilisateur1,
    age=
        st.integers(),
    nom=
        safe_text,
    adresse=
        safe_text
)

@given(instance=Trajet1_strategy)
@settings(max_examples=50)
def test_trajet1_instantiation(instance):
    assert isinstance(instance, Trajet1)



@given(instance=Trajet1_strategy)
def test_trajet1_dateFin_setter(instance):
    original = instance.dateFin
    instance.dateFin = original
    assert instance.dateFin == original



@given(instance=Trajet1_strategy)
def test_trajet1_lieudebut_setter(instance):
    original = instance.lieudebut
    instance.lieudebut = original
    assert instance.lieudebut == original



@given(instance=Trajet1_strategy)
def test_trajet1_datedebut_setter(instance):
    original = instance.datedebut
    instance.datedebut = original
    assert instance.datedebut == original



@given(instance=Trajet1_strategy)
def test_trajet1_lieuFin_setter(instance):
    original = instance.lieuFin
    instance.lieuFin = original
    assert instance.lieuFin == original

@given(instance=Trajet_strategy)
@settings(max_examples=50)
def test_trajet_instantiation(instance):
    assert isinstance(instance, Trajet)



@given(instance=Trajet_strategy)
def test_trajet_prix_setter(instance):
    original = instance.prix
    instance.prix = original
    assert instance.prix == original



@given(instance=Trajet_strategy)
def test_trajet_placesRestantes_setter(instance):
    original = instance.placesRestantes
    instance.placesRestantes = original
    assert instance.placesRestantes == original



@given(instance=Trajet_strategy)
def test_trajet_depart_setter(instance):
    original = instance.depart
    instance.depart = original
    assert instance.depart == original



@given(instance=Trajet_strategy)
def test_trajet_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Trajet_strategy)
def test_trajet_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=Trajet_strategy)
def test_trajet_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Voiture_strategy)
@settings(max_examples=50)
def test_voiture_instantiation(instance):
    assert isinstance(instance, Voiture)



@given(instance=Voiture_strategy)
def test_voiture_places_setter(instance):
    original = instance.places
    instance.places = original
    assert instance.places == original

@given(instance=Avis1_strategy)
@settings(max_examples=50)
def test_avis1_instantiation(instance):
    assert isinstance(instance, Avis1)



@given(instance=Avis1_strategy)
def test_avis1_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Avis1_strategy)
def test_avis1_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=Utilisateur_strategy)
@settings(max_examples=50)
def test_utilisateur_instantiation(instance):
    assert isinstance(instance, Utilisateur)



@given(instance=Utilisateur_strategy)
def test_utilisateur_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_photoDeProfil_setter(instance):
    original = instance.photoDeProfil
    instance.photoDeProfil = original
    assert instance.photoDeProfil == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_nbAvis_setter(instance):
    original = instance.nbAvis
    instance.nbAvis = original
    assert instance.nbAvis == original

@given(instance=Avis_strategy)
@settings(max_examples=50)
def test_avis_instantiation(instance):
    assert isinstance(instance, Avis)

@given(instance=Personne_strategy)
@settings(max_examples=50)
def test_personne_instantiation(instance):
    assert isinstance(instance, Personne)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Chemin_Interface_strategy)
@settings(max_examples=50)
def test_chemin_interface_instantiation(instance):
    assert isinstance(instance, Chemin_Interface)

@given(instance=Passager_strategy)
@settings(max_examples=50)
def test_passager_instantiation(instance):
    assert isinstance(instance, Passager)

@given(instance=Conducteur_strategy)
@settings(max_examples=50)
def test_conducteur_instantiation(instance):
    assert isinstance(instance, Conducteur)

@given(instance=Lieu_strategy)
@settings(max_examples=50)
def test_lieu_instantiation(instance):
    assert isinstance(instance, Lieu)

@given(instance=V_hicule_strategy)
@settings(max_examples=50)
def test_v_hicule_instantiation(instance):
    assert isinstance(instance, V_hicule)



@given(instance=V_hicule_strategy)
def test_v_hicule_propri_taire_setter(instance):
    original = instance.propri_taire
    instance.propri_taire = original
    assert instance.propri_taire == original



@given(instance=V_hicule_strategy)
def test_v_hicule_modele_setter(instance):
    original = instance.modele
    instance.modele = original
    assert instance.modele == original



@given(instance=V_hicule_strategy)
def test_v_hicule_marque_setter(instance):
    original = instance.marque
    instance.marque = original
    assert instance.marque == original



@given(instance=V_hicule_strategy)
def test_v_hicule_imatriculation_setter(instance):
    original = instance.imatriculation
    instance.imatriculation = original
    assert instance.imatriculation == original

@given(instance=Utilisateur1_strategy)
@settings(max_examples=50)
def test_utilisateur1_instantiation(instance):
    assert isinstance(instance, Utilisateur1)



@given(instance=Utilisateur1_strategy)
def test_utilisateur1_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Utilisateur1_strategy)
def test_utilisateur1_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Utilisateur1_strategy)
def test_utilisateur1_adresse_setter(instance):
    original = instance.adresse
    instance.adresse = original
    assert instance.adresse == original
