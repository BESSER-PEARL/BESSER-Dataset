import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data::Model,
    Data::Methode,
    Data::Attribut,
    Data::Classe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data::model_is_not_abstract():
    assert not inspect.isabstract(Data::Model)


def test_data::model_constructor_exists():
    assert callable(Data::Model.__init__)


def test_data::model_constructor_args():
    sig = inspect.signature(Data::Model.__init__)
    params = list(sig.parameters.keys())



def test_data::methode_is_not_abstract():
    assert not inspect.isabstract(Data::Methode)


def test_data::methode_constructor_exists():
    assert callable(Data::Methode.__init__)


def test_data::methode_constructor_args():
    sig = inspect.signature(Data::Methode.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "typeRetour" in params, "Missing parameter 'typeRetour'"

def test_data::methode_has_nom():
    assert hasattr(Data::Methode, "nom")
    descriptor = None
    for klass in Data::Methode.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_data::methode_has_typeRetour():
    assert hasattr(Data::Methode, "typeRetour")
    descriptor = None
    for klass in Data::Methode.__mro__:
        if "typeRetour" in klass.__dict__:
            descriptor = klass.__dict__["typeRetour"]
            break
    assert isinstance(descriptor, property)



def test_data::attribut_is_not_abstract():
    assert not inspect.isabstract(Data::Attribut)


def test_data::attribut_constructor_exists():
    assert callable(Data::Attribut.__init__)


def test_data::attribut_constructor_args():
    sig = inspect.signature(Data::Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "type" in params, "Missing parameter 'type'"

def test_data::attribut_has_nom():
    assert hasattr(Data::Attribut, "nom")
    descriptor = None
    for klass in Data::Attribut.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_data::attribut_has_type():
    assert hasattr(Data::Attribut, "type")
    descriptor = None
    for klass in Data::Attribut.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_data::classe_is_not_abstract():
    assert not inspect.isabstract(Data::Classe)


def test_data::classe_constructor_exists():
    assert callable(Data::Classe.__init__)


def test_data::classe_constructor_args():
    sig = inspect.signature(Data::Classe.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_data::classe_has_nom():
    assert hasattr(Data::Classe, "nom")
    descriptor = None
    for klass in Data::Classe.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
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
Data::Model_strategy = st.builds(
    Data::Model,
)
Data::Methode_strategy = st.builds(
    Data::Methode,
    nom=
        safe_text,
    typeRetour=
        safe_text
)
Data::Attribut_strategy = st.builds(
    Data::Attribut,
    nom=
        safe_text,
    type=
        safe_text
)
Data::Classe_strategy = st.builds(
    Data::Classe,
    nom=
        safe_text
)

@given(instance=Data::Model_strategy)
@settings(max_examples=50)
def test_data::model_instantiation(instance):
    assert isinstance(instance, Data::Model)

@given(instance=Data::Methode_strategy)
@settings(max_examples=50)
def test_data::methode_instantiation(instance):
    assert isinstance(instance, Data::Methode)

@given(instance=Data::Methode_strategy)
def test_data::methode_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=Data::Methode_strategy)
def test_data::methode_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=Data::Methode_strategy)
def test_data::methode_typeRetour_type(instance):
    assert isinstance(instance.typeRetour, str)


@given(instance=Data::Methode_strategy)
def test_data::methode_typeRetour_setter(instance):
    original = instance.typeRetour
    instance.typeRetour = original
    assert instance.typeRetour == original

@given(instance=Data::Attribut_strategy)
@settings(max_examples=50)
def test_data::attribut_instantiation(instance):
    assert isinstance(instance, Data::Attribut)

@given(instance=Data::Attribut_strategy)
def test_data::attribut_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=Data::Attribut_strategy)
def test_data::attribut_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Data::Classe_strategy)
@settings(max_examples=50)
def test_data::classe_instantiation(instance):
    assert isinstance(instance, Data::Classe)

@given(instance=Data::Classe_strategy)
def test_data::classe_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=Data::Classe_strategy)
def test_data::classe_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original
