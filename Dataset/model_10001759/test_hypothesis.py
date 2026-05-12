import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    voiture,
    conducteur,
    passager,
    inscription,
    administrateur,
    trajet,
    paiement,
    reservation,
    compte,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_voiture_is_not_abstract():
    assert not inspect.isabstract(voiture)


def test_voiture_constructor_exists():
    assert callable(voiture.__init__)


def test_voiture_constructor_args():
    sig = inspect.signature(voiture.__init__)
    params = list(sig.parameters.keys())
    assert "nombre_de_si_ges" in params, "Missing parameter 'nombre_de_si_ges'"
    assert "type_de_voiture" in params, "Missing parameter 'type_de_voiture'"

def test_voiture_has_nombre_de_si_ges():
    assert hasattr(voiture, "nombre_de_si_ges")
    descriptor = None
    for klass in voiture.__mro__:
        if "nombre_de_si_ges" in klass.__dict__:
            descriptor = klass.__dict__["nombre_de_si_ges"]
            break
    assert isinstance(descriptor, property)

def test_voiture_has_type_de_voiture():
    assert hasattr(voiture, "type_de_voiture")
    descriptor = None
    for klass in voiture.__mro__:
        if "type_de_voiture" in klass.__dict__:
            descriptor = klass.__dict__["type_de_voiture"]
            break
    assert isinstance(descriptor, property)



def test_conducteur_is_not_abstract():
    assert not inspect.isabstract(conducteur)


def test_conducteur_constructor_exists():
    assert callable(conducteur.__init__)


def test_conducteur_constructor_args():
    sig = inspect.signature(conducteur.__init__)
    params = list(sig.parameters.keys())
    assert "informations_conducteur" in params, "Missing parameter 'informations_conducteur'"

def test_conducteur_has_informations_conducteur():
    assert hasattr(conducteur, "informations_conducteur")
    descriptor = None
    for klass in conducteur.__mro__:
        if "informations_conducteur" in klass.__dict__:
            descriptor = klass.__dict__["informations_conducteur"]
            break
    assert isinstance(descriptor, property)



def test_passager_is_not_abstract():
    assert not inspect.isabstract(passager)


def test_passager_constructor_exists():
    assert callable(passager.__init__)


def test_passager_constructor_args():
    sig = inspect.signature(passager.__init__)
    params = list(sig.parameters.keys())
    assert "informations_passager" in params, "Missing parameter 'informations_passager'"

def test_passager_has_informations_passager():
    assert hasattr(passager, "informations_passager")
    descriptor = None
    for klass in passager.__mro__:
        if "informations_passager" in klass.__dict__:
            descriptor = klass.__dict__["informations_passager"]
            break
    assert isinstance(descriptor, property)



def test_inscription_is_not_abstract():
    assert not inspect.isabstract(inscription)


def test_inscription_constructor_exists():
    assert callable(inscription.__init__)


def test_inscription_constructor_args():
    sig = inspect.signature(inscription.__init__)
    params = list(sig.parameters.keys())
    assert "informations_conducteur" in params, "Missing parameter 'informations_conducteur'"
    assert "informations_passager" in params, "Missing parameter 'informations_passager'"

def test_inscription_has_informations_conducteur():
    assert hasattr(inscription, "informations_conducteur")
    descriptor = None
    for klass in inscription.__mro__:
        if "informations_conducteur" in klass.__dict__:
            descriptor = klass.__dict__["informations_conducteur"]
            break
    assert isinstance(descriptor, property)

def test_inscription_has_informations_passager():
    assert hasattr(inscription, "informations_passager")
    descriptor = None
    for klass in inscription.__mro__:
        if "informations_passager" in klass.__dict__:
            descriptor = klass.__dict__["informations_passager"]
            break
    assert isinstance(descriptor, property)



def test_administrateur_is_not_abstract():
    assert not inspect.isabstract(administrateur)


def test_administrateur_constructor_exists():
    assert callable(administrateur.__init__)


def test_administrateur_constructor_args():
    sig = inspect.signature(administrateur.__init__)
    params = list(sig.parameters.keys())



def test_trajet_is_not_abstract():
    assert not inspect.isabstract(trajet)


def test_trajet_constructor_exists():
    assert callable(trajet.__init__)


def test_trajet_constructor_args():
    sig = inspect.signature(trajet.__init__)
    params = list(sig.parameters.keys())
    assert "la_date" in params, "Missing parameter 'la_date'"
    assert "l_heure_de_d_part" in params, "Missing parameter 'l_heure_de_d_part'"
    assert "lieu_de_d_part" in params, "Missing parameter 'lieu_de_d_part'"
    assert "prix_du_trajet" in params, "Missing parameter 'prix_du_trajet'"

def test_trajet_has_la_date():
    assert hasattr(trajet, "la_date")
    descriptor = None
    for klass in trajet.__mro__:
        if "la_date" in klass.__dict__:
            descriptor = klass.__dict__["la_date"]
            break
    assert isinstance(descriptor, property)

def test_trajet_has_l_heure_de_d_part():
    assert hasattr(trajet, "l_heure_de_d_part")
    descriptor = None
    for klass in trajet.__mro__:
        if "l_heure_de_d_part" in klass.__dict__:
            descriptor = klass.__dict__["l_heure_de_d_part"]
            break
    assert isinstance(descriptor, property)

def test_trajet_has_lieu_de_d_part():
    assert hasattr(trajet, "lieu_de_d_part")
    descriptor = None
    for klass in trajet.__mro__:
        if "lieu_de_d_part" in klass.__dict__:
            descriptor = klass.__dict__["lieu_de_d_part"]
            break
    assert isinstance(descriptor, property)

def test_trajet_has_prix_du_trajet():
    assert hasattr(trajet, "prix_du_trajet")
    descriptor = None
    for klass in trajet.__mro__:
        if "prix_du_trajet" in klass.__dict__:
            descriptor = klass.__dict__["prix_du_trajet"]
            break
    assert isinstance(descriptor, property)



def test_paiement_is_not_abstract():
    assert not inspect.isabstract(paiement)


def test_paiement_constructor_exists():
    assert callable(paiement.__init__)


def test_paiement_constructor_args():
    sig = inspect.signature(paiement.__init__)
    params = list(sig.parameters.keys())
    assert "m_thode_de_paiement" in params, "Missing parameter 'm_thode_de_paiement'"

def test_paiement_has_m_thode_de_paiement():
    assert hasattr(paiement, "m_thode_de_paiement")
    descriptor = None
    for klass in paiement.__mro__:
        if "m_thode_de_paiement" in klass.__dict__:
            descriptor = klass.__dict__["m_thode_de_paiement"]
            break
    assert isinstance(descriptor, property)



def test_reservation_is_not_abstract():
    assert not inspect.isabstract(reservation)


def test_reservation_constructor_exists():
    assert callable(reservation.__init__)


def test_reservation_constructor_args():
    sig = inspect.signature(reservation.__init__)
    params = list(sig.parameters.keys())
    assert "nombre_de_passager" in params, "Missing parameter 'nombre_de_passager'"

def test_reservation_has_nombre_de_passager():
    assert hasattr(reservation, "nombre_de_passager")
    descriptor = None
    for klass in reservation.__mro__:
        if "nombre_de_passager" in klass.__dict__:
            descriptor = klass.__dict__["nombre_de_passager"]
            break
    assert isinstance(descriptor, property)



def test_compte_is_not_abstract():
    assert not inspect.isabstract(compte)


def test_compte_constructor_exists():
    assert callable(compte.__init__)


def test_compte_constructor_args():
    sig = inspect.signature(compte.__init__)
    params = list(sig.parameters.keys())
    assert "informations_passager" in params, "Missing parameter 'informations_passager'"
    assert "informations_conducteur" in params, "Missing parameter 'informations_conducteur'"

def test_compte_has_informations_passager():
    assert hasattr(compte, "informations_passager")
    descriptor = None
    for klass in compte.__mro__:
        if "informations_passager" in klass.__dict__:
            descriptor = klass.__dict__["informations_passager"]
            break
    assert isinstance(descriptor, property)

def test_compte_has_informations_conducteur():
    assert hasattr(compte, "informations_conducteur")
    descriptor = None
    for klass in compte.__mro__:
        if "informations_conducteur" in klass.__dict__:
            descriptor = klass.__dict__["informations_conducteur"]
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
voiture_strategy = st.builds(
    voiture,
    nombre_de_si_ges=
        st.integers(),
    type_de_voiture=
        safe_text
)
conducteur_strategy = st.builds(
    conducteur,
    informations_conducteur=
        safe_text
)
passager_strategy = st.builds(
    passager,
    informations_passager=
        safe_text
)
inscription_strategy = st.builds(
    inscription,
    informations_conducteur=
        safe_text,
    informations_passager=
        safe_text
)
administrateur_strategy = st.builds(
    administrateur,
)
trajet_strategy = st.builds(
    trajet,
    la_date=
        safe_text,
    l_heure_de_d_part=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lieu_de_d_part=
        safe_text,
    prix_du_trajet=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
paiement_strategy = st.builds(
    paiement,
    m_thode_de_paiement=
        safe_text
)
reservation_strategy = st.builds(
    reservation,
    nombre_de_passager=
        st.integers()
)
compte_strategy = st.builds(
    compte,
    informations_passager=
        safe_text,
    informations_conducteur=
        safe_text
)

@given(instance=voiture_strategy)
@settings(max_examples=50)
def test_voiture_instantiation(instance):
    assert isinstance(instance, voiture)



@given(instance=voiture_strategy)
def test_voiture_nombre_de_si_ges_setter(instance):
    original = instance.nombre_de_si_ges
    instance.nombre_de_si_ges = original
    assert instance.nombre_de_si_ges == original



@given(instance=voiture_strategy)
def test_voiture_type_de_voiture_setter(instance):
    original = instance.type_de_voiture
    instance.type_de_voiture = original
    assert instance.type_de_voiture == original

@given(instance=conducteur_strategy)
@settings(max_examples=50)
def test_conducteur_instantiation(instance):
    assert isinstance(instance, conducteur)



@given(instance=conducteur_strategy)
def test_conducteur_informations_conducteur_setter(instance):
    original = instance.informations_conducteur
    instance.informations_conducteur = original
    assert instance.informations_conducteur == original

@given(instance=passager_strategy)
@settings(max_examples=50)
def test_passager_instantiation(instance):
    assert isinstance(instance, passager)



@given(instance=passager_strategy)
def test_passager_informations_passager_setter(instance):
    original = instance.informations_passager
    instance.informations_passager = original
    assert instance.informations_passager == original

@given(instance=inscription_strategy)
@settings(max_examples=50)
def test_inscription_instantiation(instance):
    assert isinstance(instance, inscription)



@given(instance=inscription_strategy)
def test_inscription_informations_conducteur_setter(instance):
    original = instance.informations_conducteur
    instance.informations_conducteur = original
    assert instance.informations_conducteur == original



@given(instance=inscription_strategy)
def test_inscription_informations_passager_setter(instance):
    original = instance.informations_passager
    instance.informations_passager = original
    assert instance.informations_passager == original

@given(instance=administrateur_strategy)
@settings(max_examples=50)
def test_administrateur_instantiation(instance):
    assert isinstance(instance, administrateur)

@given(instance=trajet_strategy)
@settings(max_examples=50)
def test_trajet_instantiation(instance):
    assert isinstance(instance, trajet)



@given(instance=trajet_strategy)
def test_trajet_la_date_setter(instance):
    original = instance.la_date
    instance.la_date = original
    assert instance.la_date == original



@given(instance=trajet_strategy)
def test_trajet_l_heure_de_d_part_setter(instance):
    original = instance.l_heure_de_d_part
    instance.l_heure_de_d_part = original
    assert instance.l_heure_de_d_part == original



@given(instance=trajet_strategy)
def test_trajet_lieu_de_d_part_setter(instance):
    original = instance.lieu_de_d_part
    instance.lieu_de_d_part = original
    assert instance.lieu_de_d_part == original



@given(instance=trajet_strategy)
def test_trajet_prix_du_trajet_setter(instance):
    original = instance.prix_du_trajet
    instance.prix_du_trajet = original
    assert instance.prix_du_trajet == original

@given(instance=paiement_strategy)
@settings(max_examples=50)
def test_paiement_instantiation(instance):
    assert isinstance(instance, paiement)



@given(instance=paiement_strategy)
def test_paiement_m_thode_de_paiement_setter(instance):
    original = instance.m_thode_de_paiement
    instance.m_thode_de_paiement = original
    assert instance.m_thode_de_paiement == original

@given(instance=reservation_strategy)
@settings(max_examples=50)
def test_reservation_instantiation(instance):
    assert isinstance(instance, reservation)



@given(instance=reservation_strategy)
def test_reservation_nombre_de_passager_setter(instance):
    original = instance.nombre_de_passager
    instance.nombre_de_passager = original
    assert instance.nombre_de_passager == original

@given(instance=compte_strategy)
@settings(max_examples=50)
def test_compte_instantiation(instance):
    assert isinstance(instance, compte)



@given(instance=compte_strategy)
def test_compte_informations_passager_setter(instance):
    original = instance.informations_passager
    instance.informations_passager = original
    assert instance.informations_passager == original



@given(instance=compte_strategy)
def test_compte_informations_conducteur_setter(instance):
    original = instance.informations_conducteur
    instance.informations_conducteur = original
    assert instance.informations_conducteur == original
