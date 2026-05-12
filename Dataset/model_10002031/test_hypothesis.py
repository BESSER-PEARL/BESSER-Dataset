import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    retard,
    abs,
    reduire,
    EtatConge,
    typecong_,
    Conge,
    typeEmploy_,
    salari_,
    administrateur,
    Employ_,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_retard_is_not_abstract():
    assert not inspect.isabstract(retard)


def test_retard_constructor_exists():
    assert callable(retard.__init__)


def test_retard_constructor_args():
    sig = inspect.signature(retard.__init__)
    params = list(sig.parameters.keys())
    assert "idretad" in params, "Missing parameter 'idretad'"
    assert "nbrminute" in params, "Missing parameter 'nbrminute'"
    assert "motif" in params, "Missing parameter 'motif'"

def test_retard_has_idretad():
    assert hasattr(retard, "idretad")
    descriptor = None
    for klass in retard.__mro__:
        if "idretad" in klass.__dict__:
            descriptor = klass.__dict__["idretad"]
            break
    assert isinstance(descriptor, property)

def test_retard_has_nbrminute():
    assert hasattr(retard, "nbrminute")
    descriptor = None
    for klass in retard.__mro__:
        if "nbrminute" in klass.__dict__:
            descriptor = klass.__dict__["nbrminute"]
            break
    assert isinstance(descriptor, property)

def test_retard_has_motif():
    assert hasattr(retard, "motif")
    descriptor = None
    for klass in retard.__mro__:
        if "motif" in klass.__dict__:
            descriptor = klass.__dict__["motif"]
            break
    assert isinstance(descriptor, property)



def test_abs_is_not_abstract():
    assert not inspect.isabstract(abs)


def test_abs_constructor_exists():
    assert callable(abs.__init__)


def test_abs_constructor_args():
    sig = inspect.signature(abs.__init__)
    params = list(sig.parameters.keys())
    assert "nbrjr" in params, "Missing parameter 'nbrjr'"
    assert "idab" in params, "Missing parameter 'idab'"
    assert "motif" in params, "Missing parameter 'motif'"

def test_abs_has_nbrjr():
    assert hasattr(abs, "nbrjr")
    descriptor = None
    for klass in abs.__mro__:
        if "nbrjr" in klass.__dict__:
            descriptor = klass.__dict__["nbrjr"]
            break
    assert isinstance(descriptor, property)

def test_abs_has_idab():
    assert hasattr(abs, "idab")
    descriptor = None
    for klass in abs.__mro__:
        if "idab" in klass.__dict__:
            descriptor = klass.__dict__["idab"]
            break
    assert isinstance(descriptor, property)

def test_abs_has_motif():
    assert hasattr(abs, "motif")
    descriptor = None
    for klass in abs.__mro__:
        if "motif" in klass.__dict__:
            descriptor = klass.__dict__["motif"]
            break
    assert isinstance(descriptor, property)



def test_reduire_is_not_abstract():
    assert not inspect.isabstract(reduire)


def test_reduire_constructor_exists():
    assert callable(reduire.__init__)


def test_reduire_constructor_args():
    sig = inspect.signature(reduire.__init__)
    params = list(sig.parameters.keys())



def test_etatconge_is_not_abstract():
    assert not inspect.isabstract(EtatConge)


def test_etatconge_constructor_exists():
    assert callable(EtatConge.__init__)


def test_etatconge_constructor_args():
    sig = inspect.signature(EtatConge.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "idEtat" in params, "Missing parameter 'idEtat'"

def test_etatconge_has_nom():
    assert hasattr(EtatConge, "nom")
    descriptor = None
    for klass in EtatConge.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_etatconge_has_idEtat():
    assert hasattr(EtatConge, "idEtat")
    descriptor = None
    for klass in EtatConge.__mro__:
        if "idEtat" in klass.__dict__:
            descriptor = klass.__dict__["idEtat"]
            break
    assert isinstance(descriptor, property)



def test_typecong__is_not_abstract():
    assert not inspect.isabstract(typecong_)


def test_typecong__constructor_exists():
    assert callable(typecong_.__init__)


def test_typecong__constructor_args():
    sig = inspect.signature(typecong_.__init__)
    params = list(sig.parameters.keys())
    assert "idconge" in params, "Missing parameter 'idconge'"

def test_typecong__has_idconge():
    assert hasattr(typecong_, "idconge")
    descriptor = None
    for klass in typecong_.__mro__:
        if "idconge" in klass.__dict__:
            descriptor = klass.__dict__["idconge"]
            break
    assert isinstance(descriptor, property)



def test_conge_is_not_abstract():
    assert not inspect.isabstract(Conge)


def test_conge_constructor_exists():
    assert callable(Conge.__init__)


def test_conge_constructor_args():
    sig = inspect.signature(Conge.__init__)
    params = list(sig.parameters.keys())
    assert "datefin" in params, "Missing parameter 'datefin'"
    assert "adresse" in params, "Missing parameter 'adresse'"
    assert "datedebut" in params, "Missing parameter 'datedebut'"
    assert "id" in params, "Missing parameter 'id'"

def test_conge_has_datefin():
    assert hasattr(Conge, "datefin")
    descriptor = None
    for klass in Conge.__mro__:
        if "datefin" in klass.__dict__:
            descriptor = klass.__dict__["datefin"]
            break
    assert isinstance(descriptor, property)

def test_conge_has_adresse():
    assert hasattr(Conge, "adresse")
    descriptor = None
    for klass in Conge.__mro__:
        if "adresse" in klass.__dict__:
            descriptor = klass.__dict__["adresse"]
            break
    assert isinstance(descriptor, property)

def test_conge_has_datedebut():
    assert hasattr(Conge, "datedebut")
    descriptor = None
    for klass in Conge.__mro__:
        if "datedebut" in klass.__dict__:
            descriptor = klass.__dict__["datedebut"]
            break
    assert isinstance(descriptor, property)

def test_conge_has_id():
    assert hasattr(Conge, "id")
    descriptor = None
    for klass in Conge.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_typeemploy__is_not_abstract():
    assert not inspect.isabstract(typeEmploy_)


def test_typeemploy__constructor_exists():
    assert callable(typeEmploy_.__init__)


def test_typeemploy__constructor_args():
    sig = inspect.signature(typeEmploy_.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_typeemploy__has_id():
    assert hasattr(typeEmploy_, "id")
    descriptor = None
    for klass in typeEmploy_.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_salari__is_not_abstract():
    assert not inspect.isabstract(salari_)


def test_salari__constructor_exists():
    assert callable(salari_.__init__)


def test_salari__constructor_args():
    sig = inspect.signature(salari_.__init__)
    params = list(sig.parameters.keys())
    assert "departement" in params, "Missing parameter 'departement'"

def test_salari__has_departement():
    assert hasattr(salari_, "departement")
    descriptor = None
    for klass in salari_.__mro__:
        if "departement" in klass.__dict__:
            descriptor = klass.__dict__["departement"]
            break
    assert isinstance(descriptor, property)



def test_administrateur_is_not_abstract():
    assert not inspect.isabstract(administrateur)


def test_administrateur_constructor_exists():
    assert callable(administrateur.__init__)


def test_administrateur_constructor_args():
    sig = inspect.signature(administrateur.__init__)
    params = list(sig.parameters.keys())
    assert "secteur" in params, "Missing parameter 'secteur'"

def test_administrateur_has_secteur():
    assert hasattr(administrateur, "secteur")
    descriptor = None
    for klass in administrateur.__mro__:
        if "secteur" in klass.__dict__:
            descriptor = klass.__dict__["secteur"]
            break
    assert isinstance(descriptor, property)



def test_employ__is_not_abstract():
    assert not inspect.isabstract(Employ_)


def test_employ__constructor_exists():
    assert callable(Employ_.__init__)


def test_employ__constructor_args():
    sig = inspect.signature(Employ_.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "adresse" in params, "Missing parameter 'adresse'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "poste" in params, "Missing parameter 'poste'"

def test_employ__has_ID():
    assert hasattr(Employ_, "ID")
    descriptor = None
    for klass in Employ_.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_employ__has_adresse():
    assert hasattr(Employ_, "adresse")
    descriptor = None
    for klass in Employ_.__mro__:
        if "adresse" in klass.__dict__:
            descriptor = klass.__dict__["adresse"]
            break
    assert isinstance(descriptor, property)

def test_employ__has_nom():
    assert hasattr(Employ_, "nom")
    descriptor = None
    for klass in Employ_.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_employ__has_prenom():
    assert hasattr(Employ_, "prenom")
    descriptor = None
    for klass in Employ_.__mro__:
        if "prenom" in klass.__dict__:
            descriptor = klass.__dict__["prenom"]
            break
    assert isinstance(descriptor, property)

def test_employ__has_poste():
    assert hasattr(Employ_, "poste")
    descriptor = None
    for klass in Employ_.__mro__:
        if "poste" in klass.__dict__:
            descriptor = klass.__dict__["poste"]
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
retard_strategy = st.builds(
    retard,
    idretad=
        st.integers(),
    nbrminute=
        st.integers(),
    motif=
        safe_text
)
abs_strategy = st.builds(
    abs,
    nbrjr=
        st.integers(),
    idab=
        st.integers(),
    motif=
        safe_text
)
reduire_strategy = st.builds(
    reduire,
)
EtatConge_strategy = st.builds(
    EtatConge,
    nom=
        safe_text,
    idEtat=
        st.integers()
)
typecong__strategy = st.builds(
    typecong_,
    idconge=
        st.integers()
)
Conge_strategy = st.builds(
    Conge,
    datefin=
        safe_text,
    adresse=
        safe_text,
    datedebut=
        safe_text,
    id=
        st.integers()
)
typeEmploy__strategy = st.builds(
    typeEmploy_,
    id=
        safe_text
)
salari__strategy = st.builds(
    salari_,
    departement=
        safe_text
)
administrateur_strategy = st.builds(
    administrateur,
    secteur=
        safe_text
)
Employ__strategy = st.builds(
    Employ_,
    ID=
        st.integers(),
    adresse=
        safe_text,
    nom=
        safe_text,
    prenom=
        safe_text,
    poste=
        safe_text
)

@given(instance=retard_strategy)
@settings(max_examples=50)
def test_retard_instantiation(instance):
    assert isinstance(instance, retard)



@given(instance=retard_strategy)
def test_retard_idretad_setter(instance):
    original = instance.idretad
    instance.idretad = original
    assert instance.idretad == original



@given(instance=retard_strategy)
def test_retard_nbrminute_setter(instance):
    original = instance.nbrminute
    instance.nbrminute = original
    assert instance.nbrminute == original



@given(instance=retard_strategy)
def test_retard_motif_setter(instance):
    original = instance.motif
    instance.motif = original
    assert instance.motif == original

@given(instance=abs_strategy)
@settings(max_examples=50)
def test_abs_instantiation(instance):
    assert isinstance(instance, abs)



@given(instance=abs_strategy)
def test_abs_nbrjr_setter(instance):
    original = instance.nbrjr
    instance.nbrjr = original
    assert instance.nbrjr == original



@given(instance=abs_strategy)
def test_abs_idab_setter(instance):
    original = instance.idab
    instance.idab = original
    assert instance.idab == original



@given(instance=abs_strategy)
def test_abs_motif_setter(instance):
    original = instance.motif
    instance.motif = original
    assert instance.motif == original

@given(instance=reduire_strategy)
@settings(max_examples=50)
def test_reduire_instantiation(instance):
    assert isinstance(instance, reduire)

@given(instance=EtatConge_strategy)
@settings(max_examples=50)
def test_etatconge_instantiation(instance):
    assert isinstance(instance, EtatConge)



@given(instance=EtatConge_strategy)
def test_etatconge_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=EtatConge_strategy)
def test_etatconge_idEtat_setter(instance):
    original = instance.idEtat
    instance.idEtat = original
    assert instance.idEtat == original

@given(instance=typecong__strategy)
@settings(max_examples=50)
def test_typecong__instantiation(instance):
    assert isinstance(instance, typecong_)



@given(instance=typecong__strategy)
def test_typecong__idconge_setter(instance):
    original = instance.idconge
    instance.idconge = original
    assert instance.idconge == original

@given(instance=Conge_strategy)
@settings(max_examples=50)
def test_conge_instantiation(instance):
    assert isinstance(instance, Conge)



@given(instance=Conge_strategy)
def test_conge_datefin_setter(instance):
    original = instance.datefin
    instance.datefin = original
    assert instance.datefin == original



@given(instance=Conge_strategy)
def test_conge_adresse_setter(instance):
    original = instance.adresse
    instance.adresse = original
    assert instance.adresse == original



@given(instance=Conge_strategy)
def test_conge_datedebut_setter(instance):
    original = instance.datedebut
    instance.datedebut = original
    assert instance.datedebut == original



@given(instance=Conge_strategy)
def test_conge_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=typeEmploy__strategy)
@settings(max_examples=50)
def test_typeemploy__instantiation(instance):
    assert isinstance(instance, typeEmploy_)



@given(instance=typeEmploy__strategy)
def test_typeemploy__id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=salari__strategy)
@settings(max_examples=50)
def test_salari__instantiation(instance):
    assert isinstance(instance, salari_)



@given(instance=salari__strategy)
def test_salari__departement_setter(instance):
    original = instance.departement
    instance.departement = original
    assert instance.departement == original

@given(instance=administrateur_strategy)
@settings(max_examples=50)
def test_administrateur_instantiation(instance):
    assert isinstance(instance, administrateur)



@given(instance=administrateur_strategy)
def test_administrateur_secteur_setter(instance):
    original = instance.secteur
    instance.secteur = original
    assert instance.secteur == original

@given(instance=Employ__strategy)
@settings(max_examples=50)
def test_employ__instantiation(instance):
    assert isinstance(instance, Employ_)



@given(instance=Employ__strategy)
def test_employ__ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Employ__strategy)
def test_employ__adresse_setter(instance):
    original = instance.adresse
    instance.adresse = original
    assert instance.adresse == original



@given(instance=Employ__strategy)
def test_employ__nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Employ__strategy)
def test_employ__prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=Employ__strategy)
def test_employ__poste_setter(instance):
    original = instance.poste
    instance.poste = original
    assert instance.poste == original
