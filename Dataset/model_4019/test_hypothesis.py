import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Data_Model,
    Data_Methode,
    Data_Attribut,
    Data_Classe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_model_is_not_abstract():
    assert not inspect.isabstract(Data_Model)


def test_data_model_constructor_exists():
    assert callable(Data_Model.__init__)


def test_data_model_constructor_args():
    sig = inspect.signature(Data_Model.__init__)
    params = list(sig.parameters.keys())



def test_data_methode_is_not_abstract():
    assert not inspect.isabstract(Data_Methode)


def test_data_methode_constructor_exists():
    assert callable(Data_Methode.__init__)


def test_data_methode_constructor_args():
    sig = inspect.signature(Data_Methode.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "typeRetour" in params, "Missing parameter 'typeRetour'"

def test_data_methode_has_nom():
    assert hasattr(Data_Methode, "nom")
    descriptor = None
    for klass in Data_Methode.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_data_methode_has_typeRetour():
    assert hasattr(Data_Methode, "typeRetour")
    descriptor = None
    for klass in Data_Methode.__mro__:
        if "typeRetour" in klass.__dict__:
            descriptor = klass.__dict__["typeRetour"]
            break
    assert isinstance(descriptor, property)



def test_data_attribut_is_not_abstract():
    assert not inspect.isabstract(Data_Attribut)


def test_data_attribut_constructor_exists():
    assert callable(Data_Attribut.__init__)


def test_data_attribut_constructor_args():
    sig = inspect.signature(Data_Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "nom" in params, "Missing parameter 'nom'"

def test_data_attribut_has_type():
    assert hasattr(Data_Attribut, "type")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_data_attribut_has_nom():
    assert hasattr(Data_Attribut, "nom")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_data_classe_is_not_abstract():
    assert not inspect.isabstract(Data_Classe)


def test_data_classe_constructor_exists():
    assert callable(Data_Classe.__init__)


def test_data_classe_constructor_args():
    sig = inspect.signature(Data_Classe.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_data_classe_has_nom():
    assert hasattr(Data_Classe, "nom")
    descriptor = None
    for klass in Data_Classe.__mro__:
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
Data_Model_strategy = st.builds(
    Data_Model,
)
Data_Methode_strategy = st.builds(
    Data_Methode,
    nom=
        safe_text,
    typeRetour=
        safe_text
)
Data_Attribut_strategy = st.builds(
    Data_Attribut,
    type=
        safe_text,
    nom=
        safe_text
)
Data_Classe_strategy = st.builds(
    Data_Classe,
    nom=
        safe_text
)

@given(instance=Data_Model_strategy)
@settings(max_examples=50)
def test_data_model_instantiation(instance):
    assert isinstance(instance, Data_Model)

@given(instance=Data_Methode_strategy)
@settings(max_examples=50)
def test_data_methode_instantiation(instance):
    assert isinstance(instance, Data_Methode)



@given(instance=Data_Methode_strategy)
def test_data_methode_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Data_Methode_strategy)
def test_data_methode_typeRetour_setter(instance):
    original = instance.typeRetour
    instance.typeRetour = original
    assert instance.typeRetour == original

@given(instance=Data_Attribut_strategy)
@settings(max_examples=50)
def test_data_attribut_instantiation(instance):
    assert isinstance(instance, Data_Attribut)



@given(instance=Data_Attribut_strategy)
def test_data_attribut_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Data_Attribut_strategy)
def test_data_attribut_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=Data_Classe_strategy)
@settings(max_examples=50)
def test_data_classe_instantiation(instance):
    assert isinstance(instance, Data_Classe)



@given(instance=Data_Classe_strategy)
def test_data_classe_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original
